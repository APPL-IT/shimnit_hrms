import frappe
from frappe import _
from frappe.custom.doctype.custom_field.custom_field import create_custom_field
from frappe.custom.doctype.property_setter.property_setter import make_property_setter
from frappe.utils.fixtures import sync_fixtures
from .payment_reconciliation import *

@frappe.whitelist()
def custom_field():
    payment_reconciliation_custom_fields()
    delete_custom_fields_list()

def delete_custom_fields_list():
    pass
    # if frappe.db.exists("Custom Field","Payment Reconciliation-custom_calculate_total"):
    #     frappe.delete_doc("Custom Field","Payment Reconciliation-custom_calculate_total")
    # if frappe.db.exists("Custom Field","Payment Reconciliation-custom_calculate_total_clear"):
    #     frappe.delete_doc("Custom Field","Payment Reconciliation-custom_calculate_total_clear")
    # if frappe.db.exists("Custom Field","Payment Reconciliation-custom_selected_total_value"):
    #     frappe.delete_doc("Custom Field","Payment Reconciliation-custom_selected_total_value")

