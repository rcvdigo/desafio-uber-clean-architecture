from flask import Blueprint


user_route_bp = Blueprint("user_routes", __name__) # Apelidando o @app para @user_route_bp

@user_route_bp.route("/api/email", methods=["GET"])
def find_user():
    pass
