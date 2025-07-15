app_name = "shimnit_hrms"
app_title = "Shimnit HRMS"
app_publisher = "Midocean Technolgies Pvt LTD"
app_description = "Shimnit HRMS"
app_email = "info@midocean.tech"
app_license = "mit"

fixtures = [
				{
                    "dt": "Property Setter", "filters": {"module": 'Shimnit HRMS'}
				},
                {
                    "dt": "Print Format", "filters": {"module": 'Shimnit HRMS'}
				}
			]
# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "shimnit_hrms",
# 		"logo": "/assets/shimnit_hrms/logo.png",
# 		"title": "Shimnit HRMS",
# 		"route": "/shimnit_hrms",
# 		"has_permission": "shimnit_hrms.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/shimnit_hrms/css/shimnit_hrms.css"
# app_include_js = "/assets/shimnit_hrms/js/shimnit_hrms.js"

# include js, css files in header of web template
# web_include_css = "/assets/shimnit_hrms/css/shimnit_hrms.css"
# web_include_js = "/assets/shimnit_hrms/js/shimnit_hrms.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "shimnit_hrms/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}
# include js in doctype views
doctype_js = {"Salary Slip" : "shimnit_hrms/customizations/salary_slip/salary_slip.js",
    		 "Payment Reconciliation":"shimnit_hrms/custom_script/payment_reconciliation/payment_reconciliation.js"
    }
doctype_list_js = {"Payroll Entry" : "shimnit_hrms/customizations/payroll_entry/payroll_entry_list.js"}

# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "shimnit_hrms/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "shimnit_hrms.utils.jinja_methods",
# 	"filters": "shimnit_hrms.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "shimnit_hrms.install.before_install"
# after_install = "shimnit_hrms.install.after_install"

after_install = ["shimnit_hrms.custom_fields.custom_fields.custom_field"]

after_migrate = ["shimnit_hrms.custom_fields.custom_fields.custom_field"]

# Uninstallation
# ------------

# before_uninstall = "shimnit_hrms.uninstall.before_uninstall"
# after_uninstall = "shimnit_hrms.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "shimnit_hrms.utils.before_app_install"
# after_app_install = "shimnit_hrms.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "shimnit_hrms.utils.before_app_uninstall"
# after_app_uninstall = "shimnit_hrms.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "shimnit_hrms.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }
override_doctype_class = {
    "Payroll Entry":"shimnit_hrms.shimnit_hrms.customizations.payroll_entry.payroll_entry.CustomPayrollEntry"
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Salary Slip": {
		"validate": "shimnit_hrms.shimnit_hrms.customizations.salary_slip.salary_slip.validate"
	},
    "Employee Checkin": {
		"validate": "shimnit_hrms.shimnit_hrms.customizations.employee_checkin.employee_checkin.validate"
	},
    "Journal Entry": {
		"validate": "shimnit_hrms.shimnit_hrms.customizations.journal_entry.journal_entry.validate"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"shimnit_hrms.tasks.all"
# 	],
# 	"daily": [
# 		"shimnit_hrms.tasks.daily"
# 	],
# 	"hourly": [
# 		"shimnit_hrms.tasks.hourly"
# 	],
# 	"weekly": [
# 		"shimnit_hrms.tasks.weekly"
# 	],
# 	"monthly": [
# 		"shimnit_hrms.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "shimnit_hrms.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "shimnit_hrms.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "shimnit_hrms.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["shimnit_hrms.utils.before_request"]
# after_request = ["shimnit_hrms.utils.after_request"]

# Job Events
# ----------
# before_job = ["shimnit_hrms.utils.before_job"]
# after_job = ["shimnit_hrms.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"shimnit_hrms.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

