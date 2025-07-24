frappe.ui.form.on('Salary Slip', {
    refresh(frm) {
        // Hide earnings rows
        frm.fields_dict['earnings'].grid.grid_rows.forEach(function (grid_row) {
            const row_data = grid_row.doc;
            if (row_data.custom_hide_from_salary_slip == 1) {
                grid_row.wrapper.hide();
            } else {
                grid_row.wrapper.show();
            }
        });

        // Hide deductions rows
        frm.fields_dict['deductions'].grid.grid_rows.forEach(function (grid_row) {
            const row_data = grid_row.doc;
            if (row_data.custom_hide_from_salary_slip == 1) {
                grid_row.wrapper.hide();
            } else {
                grid_row.wrapper.show();
            }
        });
    }
});
