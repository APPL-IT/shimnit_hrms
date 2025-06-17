import frappe

def validate(doc, method):
    ref_list = []
    for i in doc.accounts:
        if i.reference_type:
            ref_list.append(i.reference_type)
    if "Payroll Entry" in ref_list:
        df = doc.meta.get_field("custom_state")
        if df:
            df.reqd = 0 