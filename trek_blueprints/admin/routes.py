from flask import Blueprint

admin_bp = Blueprint(
    'admin', __name__,
    template_folder='templates',
    static_folder='static'
)

@admin_bp.route('/admin')
def admin_home():
    return f"Welcome to the admin page."