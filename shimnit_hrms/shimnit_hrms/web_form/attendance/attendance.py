import frappe

def get_context(context):
	# do your magic here
	pass


@frappe.whitelist()
def fetch_employee_name(employee):
	return frappe.get_value("Employee", employee, "employee_name")