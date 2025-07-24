frappe.ui.form.on('Salary Slip', {
    refresh(frm) {
        frm.fields_dict['earnings'].grid.wrapper.find('.grid-row').each(function (i, row_el) {
            const row_data = frm.doc.earnings[i-1];
            if (row_data && row_data.custom_hide_from_salary_slip == 1) {
                $(row_el).hide(); // hide the HTML element
            }
        });
        frm.fields_dict['deductions'].grid.wrapper.find('.grid-row').each(function (i, row_el) {
            const row_data = frm.doc.earnings[i-1];
            if (row_data && row_data.custom_hide_from_salary_slip == 1) {
                $(row_el).hide(); // hide the HTML element
            }
        });
    }
});