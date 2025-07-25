
frappe.ready(function() {
	 setTimeout(() => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    const latitude = position.coords.latitude;
                    const longitude = position.coords.longitude;

                    // Set latitude and longitude in web form
                    frappe.web_form.set_value('latitude', latitude);
                    frappe.web_form.set_value('longitude', longitude);
                },
                (error) => {
                    console.error("Geolocation error:", error.message);
                    frappe.msgprint("Unable to fetch location. Please allow location access.");
                }
            );
        } else {
            frappe.msgprint("Geolocation is not supported by your browser.");
        }

        // for server date and time
        frappe.call({
            method: "shimnit_hrms.api.utils.custom_get_server_datetime",
            callback: function(response) {
                if (response.message){
                        frappe.web_form.set_value('time', (response.message));

                }else{

                }
            }
        });
    }, 500);
	
    $(document).on('change', '[data-fieldname = "employee"]', function (event) {
        var employee = frappe.web_form.fields_dict.employee.get_value();

        frappe.call({
                method: "shimnit_hrms.shimnit_hrms.web_form.attendance.attendance.fetch_employee_name",
                args: {
                    employee : employee,
                },
                callback: function(response) {
                    if (response.message) {
                        frappe.web_form.fields_dict.employee_name.set_value(response.message);

                    } else {
                        console.error("Error fetching items:", response.message.error || "Unknown error");
                    }

                    frappe.web_form.fields_dict.employee_name.refresh();

                }
                
            });
            
        });
});
function formatDateTime(serverDatetime) {
    const dateOnly = serverDatetime.split(" ")[0]; // "2025-07-24"
    const [year, month, day] = dateOnly.split("-");
    return `${day}-${month}-${year}`;
}