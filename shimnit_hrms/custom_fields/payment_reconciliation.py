import frappe
from frappe import _
from frappe.custom.doctype.custom_field.custom_field import create_custom_field
from frappe.custom.doctype.property_setter.property_setter import make_property_setter

@frappe.whitelist()
def payment_reconciliation_custom_fields():
        # pass
    create_custom_field(
        "Payment Reconciliation",
        {
            "fieldname": "custom_calculate_total",
            "fieldtype": "Button",
            "label": "Calculate Selection",
            "insert_after": "invoice_name"
        }
    )
    create_custom_field(
        "Payment Reconciliation",
        {
            "fieldname": "custom_calculate_total_clear",
            "fieldtype": "Button",
            "label": "Clear Selection",
            "insert_after": "custom_calculate_total"
        }
    )
    create_custom_field(
        "Payment Reconciliation",
        {
            "fieldname": "custom_selected_total_value",
            "fieldtype": "HTML",
            "label": "Selected Total Value",
            "insert_after": "custom_calculate_total_clear"
        }
    )
    
    
    
