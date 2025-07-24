import frappe
from frappe.utils import now_datetime, nowdate

@frappe.whitelist()
def custom_get_server_datetime():
    return now_datetime().strftime("%Y-%m-%d %H:%M:%S")
    