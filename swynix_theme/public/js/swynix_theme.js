frappe.ready(function() {
    // Override ERPNext app name on desk
    $(document).ready(function() {
        // Change app name in selector
        setTimeout(function() {
            $('a[data-name="erpnext"]').each(function() {
                $(this).find('.app-name').text('SwynixERP');
                $(this).find('.app-icon').attr('src', '/assets/swynix_theme/images/swynix-logo.png');
            });
            
            // Update any text that says ERPNext
            $('.erpnext-app').text('SwynixERP');
        }, 500);
    });
});
