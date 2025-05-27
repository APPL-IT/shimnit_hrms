import frappe
from datetime import datetime

def validate(doc, method):

    date_obj = datetime.strptime(doc.end_date, "%Y-%m-%d")
    doc.custom_month = date_obj.strftime("%B")
    salary_structure_doc = frappe.get_doc("Salary Structure", doc.salary_structure)
    hidden_earning_comps = []
    hidden_deduction_comps = []
    for ec in salary_structure_doc.earnings:
        if ec.custom_hide_from_salary_slip == 1:
            hidden_earning_comps.append(ec.salary_component)

    for dc in salary_structure_doc.deductions:
        if dc.custom_hide_from_salary_slip == 1:
            hidden_deduction_comps.append(dc.salary_component)

    earning_rows_to_remove = []
    for i in doc.earnings:
        if i.salary_component in hidden_earning_comps:
            earning_rows_to_remove.append(i)

    for row in earning_rows_to_remove:
        doc.earnings.remove(row)

    deduction_rows_to_remove = []
    for j in doc.deductions:
        if j.salary_component in hidden_deduction_comps:
            deduction_rows_to_remove.append(j)
    
    for row1 in deduction_rows_to_remove:
        doc.deductions.remove(row1)
