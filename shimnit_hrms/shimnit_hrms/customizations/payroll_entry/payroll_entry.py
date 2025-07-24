import frappe
import erpnext
from frappe import _
from hrms.payroll.doctype.payroll_entry.payroll_entry import PayrollEntry
from erpnext.accounts.doctype.accounting_dimension.accounting_dimension import (
	get_accounting_dimensions,
)
import json

from frappe.utils import (
	DATE_FORMAT,
	add_days,
	add_to_date,
	cint,
	comma_and,
	date_diff,
	flt,
	get_link_to_form,
	getdate,
)
from datetime import timedelta

from hrms.payroll.doctype.salary_slip.salary_slip_loan_utils import if_lending_app_installed
from hrms.payroll.doctype.salary_withholding.salary_withholding import link_bank_entry_in_salary_withholdings


class CustomPayrollEntry(PayrollEntry):
	def make_accrual_jv_entry(self, submitted_salary_slips):
		self.check_permission("write")
		employee_wise_accounting_enabled = frappe.db.get_single_value(
			"Payroll Settings", "process_payroll_accounting_entry_based_on_employee"
		)
		self.employee_based_payroll_payable_entries = {}
		self._advance_deduction_entries = []

		earnings = (
			self.get_salary_component_total(
				component_type="earnings",
				employee_wise_accounting_enabled=employee_wise_accounting_enabled,
			)
			or {}
		)

		deductions = (
			self.get_salary_component_total(
				component_type="deductions",
				employee_wise_accounting_enabled=employee_wise_accounting_enabled,
			)
			or {}
		)

		precision = frappe.get_precision("Journal Entry Account", "debit_in_account_currency")

		if earnings or deductions:
			accounts = []
			currencies = []
			payable_amount = 0
			accounting_dimensions = get_accounting_dimensions() or []
			company_currency = erpnext.get_company_currency(self.company)

			payable_amount = self.get_payable_amount_for_earnings_and_deductions(
				accounts,
				earnings,
				deductions,
				currencies,
				company_currency,
				accounting_dimensions,
				precision,
				payable_amount,
			)

			payable_amount = self.set_accounting_entries_for_advance_deductions(
				accounts,
				currencies,
				company_currency,
				accounting_dimensions,
				precision,
				payable_amount,
			)

			self.set_payable_amount_against_payroll_payable_account(
				accounts,
				currencies,
				company_currency,
				accounting_dimensions,
				precision,
				payable_amount,
				self.payroll_payable_account,
				employee_wise_accounting_enabled,
			)

			self.custom_make_journal_entry(
				accounts,
				currencies,
				self.payroll_payable_account,
				voucher_type="Journal Entry",
				user_remark=_("Accrual Journal Entry for salaries from {0} to {1}").format(
					self.start_date, self.end_date
				),
				submit_journal_entry=False,
				submitted_salary_slips=submitted_salary_slips,
			)
            
	
	def custom_make_journal_entry(
		self,
		accounts,
		currencies,
		payroll_payable_account=None,
		voucher_type="Journal Entry",
		user_remark="",
		submitted_salary_slips: list | None = None,
		submit_journal_entry=False,
	) -> str:
		multi_currency = 0
		if len(currencies) > 1:
			multi_currency = 1

		journal_entry = frappe.new_doc("Journal Entry")
		journal_entry.voucher_type = voucher_type
		journal_entry.user_remark = user_remark
		journal_entry.company = self.company
		journal_entry.posting_date = self.posting_date
		journal_entry.custom_state = self.state

		journal_entry.set("accounts", accounts)
		journal_entry.multi_currency = multi_currency

		if voucher_type == "Journal Entry":
			journal_entry.title = payroll_payable_account

		journal_entry.save(ignore_permissions=True)

		try:
			if submit_journal_entry:
				journal_entry.submit()

			if submitted_salary_slips:
				self.set_journal_entry_in_salary_slips(submitted_salary_slips, jv_name=journal_entry.name)

		except Exception as e:
			if type(e) in (str, list, tuple):
				frappe.msgprint(e)

			self.log_error("Journal Entry creation against Salary Slip failed")
			raise

		return journal_entry
	
	def get_payroll_dates_for_employee(self, employee_details: dict) -> tuple[str, str]:
		start_date = self.start_date - timedelta(days=6)
		if employee_details.date_of_joining > getdate(self.start_date):
			start_date = employee_details.date_of_joining

		end_date = self.end_date - timedelta(days=6)
		if employee_details.relieving_date and employee_details.relieving_date < getdate(self.end_date):
			end_date = employee_details.relieving_date

		return start_date, end_date
 


@frappe.whitelist()
def create_bulk_payroll_entry(posting_date, start_date, end_date):
    state_list = frappe.get_all("State")
    shimnit_payroll_setting = frappe.get_doc("Shimnit Payroll Setting", "Shimnit Payroll Setting")

    if not shimnit_payroll_setting.default_payroll_payable_account:
        frappe.throw("Kindly Add Deafult Payroll Payable Account in shimnit Payroll Setting")
    if not shimnit_payroll_setting.default_payment_account:
        frappe.throw("Kindly Add Deafult Payment Account in shimnit Payroll Setting")
    if not shimnit_payroll_setting.default_bank_account:
        frappe.throw("Kindly Add Deafult Bank Account in shimnit Payroll Setting")

    emp_count = 0
    for i in state_list:
        state_wise_emp_list = frappe.get_all("Employee", filters={"custom_state": i.name, "status": "Active"})
        if len(state_wise_emp_list) > 0:
            doc = frappe.new_doc("Payroll Entry")
            doc.posting_date = posting_date
            doc.payroll_frequency = "Monthly"
            doc.currency = "INR"
            doc.exchange_rate = 1
            doc.start_date = start_date
            doc.end_date = end_date
            doc.state = i.name
            doc.payroll_payable_account = shimnit_payroll_setting.default_payroll_payable_account
            doc.payment_account = shimnit_payroll_setting.default_payment_account
            doc.bank_account = shimnit_payroll_setting.default_bank_account

            state_wise_emp_list = frappe.get_all("Employee", filters={"custom_state": i.name, "status": "Active"})
            for j in state_wise_emp_list:
                doc.append("employees",{
                    "employee": j.name
                })
            doc.insert(ignore_permissions=True)
            emp_count += len(state_wise_emp_list)
    return emp_count