frappe.ui.form.on('Salary Slip', {
    refresh(frm) {
        // Hide earnings rows with custom_hide_from_salary_slip == 1
        frm.fields_dict['earnings'].grid.wrapper.find('.grid-row').each(function (i, row_el) {
            const row_data = frm.doc.earnings[i]; // use i directly
            if (row_data && row_data.custom_hide_from_salary_slip == 1) {
                $(row_el).hide();
            } else {
                $(row_el).show();  // ensure rows not matching are visible
            }
        });

        // Hide deductions rows with custom_hide_from_salary_slip == 1
        frm.fields_dict['deductions'].grid.wrapper.find('.grid-row').each(function (i, row_el) {
            const row_data = frm.doc.deductions[i]; // use deductions here
            if (row_data && row_data.custom_hide_from_salary_slip == 1) {
                $(row_el).hide();
            } else {
                $(row_el).show();
            }
        });
    }
});
