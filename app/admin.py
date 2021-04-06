from flask import Blueprint

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/test", methods=["POST"])
def ad():
    return "This is admin test."
