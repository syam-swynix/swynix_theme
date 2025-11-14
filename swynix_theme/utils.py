import frappe

def get_website_context(context):
    """
    Add custom context to website
    """
    context.update({
        "brand_name": "Swynix",
        "brand_html": "<strong>SWYNIX</strong>",
    })
    return context
