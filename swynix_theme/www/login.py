import frappe

no_cache = 1

def get_context(context):
    if frappe.session.user != "Guest":
        frappe.local.flags.redirect_location = "/app"
        raise frappe.Redirect
    
    context.no_header = True
    context.no_breadcrumbs = True
    
    return context
