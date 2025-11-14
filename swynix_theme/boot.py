import frappe

def boot_session(bootinfo):
    """Override app name in boot session"""
    if bootinfo.get("app"):
        # Find ERPNext in installed apps and rename it
        for app in bootinfo.get("app", []):
            if app.get("name") == "erpnext":
                app["title"] = "SwynixERP"
                app["icon"] = "/assets/swynix_theme/images/swynix-logo.png"
