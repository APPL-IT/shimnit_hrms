import frappe

def validate(doc, method):
    if type(doc.time) == str:
        punch_date = doc.time.split(" ")[0]
    else:
        date_str = doc.time.strftime("%Y-%m-%d %H:%M:%S")
        punch_date = date_str.split(" ")[0]
    strt_date = punch_date + " 00:00:01"
    end_date = punch_date + " 23:59:59"
    
    checkin_list = frappe.get_all("Employee Checkin", filters={'employee': doc.employee, 'time': ['between', [strt_date, end_date]]})
    for i in checkin_list:
        checkin_doc = frappe.get_doc("Employee Checkin", i.name)
        if checkin_doc.name == doc.name:
            checkin_doc.db_set("log_type", "OUT")
        else:
            checkin_doc.db_set("log_type", "IN")
    
    if len(checkin_list) == 0:
        if doc.is_new():
            doc.log_type = "IN"
        else:
            doc.db_set("log_type" , "IN")
    else:
        doc.db_set("log_type" , "OUT")
    