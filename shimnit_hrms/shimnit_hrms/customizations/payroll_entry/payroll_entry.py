import frappe

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

    for i in state_list:
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