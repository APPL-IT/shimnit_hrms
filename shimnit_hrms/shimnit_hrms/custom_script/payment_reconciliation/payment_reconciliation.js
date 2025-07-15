frappe.ui.form.on("Payment Reconciliation", {
    refresh(frm){
        let btn1 = frm.fields_dict.custom_calculate_total.$wrapper;
        let btn2 = frm.fields_dict.custom_calculate_total_clear.$wrapper;

        // $btn.insertAfter(frm.fields_dict.custom_calculate_total.wrapper);
        $(frm.fields_dict.custom_selected_total_value.wrapper).html(format_currency(0)+" - "+format_currency(0) + " = "+format_currency(0));
        
        btn1.find("button").addClass('btn btn-xs btn-primary');
        btn2.find("button").addClass('btn btn-xs btn-danger');

    },
    
    custom_calculate_total(frm){
        let selected_invoce_total = frm.fields_dict.invoices.grid.get_selected_children();
        let selected_payments_total = frm.fields_dict.payments.grid.get_selected_children();
        if (selected_payments_total.length === 0  && selected_invoce_total.length === 0 ){
            $(frm.fields_dict.custom_selected_total_value.wrapper).html(format_currency(0)+" - "+format_currency(0) + " = "+format_currency(0));
            frappe.msgprint(__("Please Select Payment or Invoice"));
            return;
        }
        let total_invoice_value =0;
        selected_invoce_total.forEach(element => total_invoice_value += flt(element.outstanding_amount));
        
        let total_payments_value =0;
        selected_payments_total.forEach(element => total_payments_value += flt(element.amount));
        let diff_value = 0;
        diff_value = total_invoice_value - total_payments_value  ; 
        $(frm.fields_dict.custom_selected_total_value.wrapper).html(format_currency(total_invoice_value) + " - "+ format_currency(total_payments_value) + " = " + format_currency(diff_value));


    },
    custom_calculate_total_clear(frm){
        const grid_invoices = frm.fields_dict.invoices.grid;
        const selected_payments = frm.fields_dict.payments.grid;
        grid_invoices.grid_rows.forEach(row => {
            row.wrapper.find(':checkbox').prop('checked', false);
            row.doc.__checked = false;  // Optional: update grid row state
        });
        selected_payments.grid_rows.forEach(row => {
            row.wrapper.find(':checkbox').prop('checked', false);
            row.doc.__checked = false;  // Optional: update grid row state
        });
        
        $(frm.fields_dict.custom_selected_total_value.wrapper).html(format_currency(0)+" - "+format_currency(0) + " = "+format_currency(0));
        
    }

})


