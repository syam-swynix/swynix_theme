app_name = "SwynixERP"
app_title = "Swynix"
app_publisher = "Swynix"
app_description = "Custom theme and branding for Swynix"
app_email = "syam@swynix.com"
app_license = "MIT"
# Website settings
# ------------------

website_route_rules = [
    {"from_route": "/login", "to_route": "login"},
]
# This tells Frappe to use our custom login page
# Add this section to override ERPNext app details
override_doctype_dashboards = {
    "ERPNext": "swynix_theme.swynix_theme.dashboard.get_dashboard_for_erpnext"
}

# Add boot session override
extend_bootinfo = "swynix_theme.boot.boot_session"

# Override app logo
app_logo_url = "/assets/swynix_theme/images/swynix-logo.png"
###################
app_include_js = "/assets/swynix_theme/js/swynix_theme.js"
