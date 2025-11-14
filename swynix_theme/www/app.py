import frappe

def get_context(context):
    if frappe.session.user == "Guest":
        frappe.local.flags.redirect_location = "/login"
        raise frappe.Redirect
    
    # Override app name
    context.app_name = "SwynixERP"
    context.app_logo = "/assets/swynix_theme/images/swynix-logo.png"
    
    return context
