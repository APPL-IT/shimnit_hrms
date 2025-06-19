frappe.listview_settings["Payroll Entry"] = {
    onload: function (listview) {
        listview.page.add_inner_button(__('Create Bulk Payroll Entry'),function() {

            create_bulk_payroll_entry()
        },);
    },
};	

function create_bulk_payroll_entry(){
    let d = new frappe.ui.Dialog({
        title: 'Enter details',
        fields: [
            {
                label: 'Posting Date',
                fieldname: 'posting_date',
                fieldtype: 'Date',
                reqd: 1,
                default:frappe.datetime.get_today(),
                
            },
            {
                label: 'Start Date',
                fieldname: 'start_date',
                fieldtype: 'Date',
                reqd: 1,
            },
            {
                label: 'End Date',
                fieldname: 'end_date',
                fieldtype: 'Date',
                reqd: 1,
            }
        ],

    
        primary_action_label: 'Create Payroll Entry',
        primary_action: function () {
            var posting_date = d.get_values().posting_date
            var start_date = d.get_values().start_date
            var end_date = d.get_values().end_date

            frappe.call({
            method: "shimnit_hrms.shimnit_hrms.customizations.payroll_entry.payroll_entry.create_bulk_payroll_entry",
            args:{
                posting_date : posting_date,
                start_date : start_date,
                end_date : end_date,
            },
            freeze: true,
            freeze_message: __("Creating Payroll Entries ..."),
            callback: function(r) {
                frappe.msgprint("Payroll Entry Created Successfully !")
                }
            });
            d.hide();
        },
    });

    d.show();
}
