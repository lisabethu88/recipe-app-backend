from flask import Blueprint

users_bp = Blueprint("users", __name__)
@users_bp.route("/register", methods=["POST"])
def register():
    return "user registered!"

@users_bp.route("/login", methods=["POST"])
def login():
    return "user logged in!"

@users_bp.route("/logout", methods=["POST"])
def logout():
    return  "user logged out!"

# favorites routes
@users_bp.route("/users/<int:user_id>/favorites", methods=["GET"])
def get_all_favorites(user_id):
    return 'favorites' + str(user_id)

@users_bp.route("/users/<int:user_id>/favorites", methods=["POST"])
def create_favorite(user_id):
    return 'favorite created! ' + str(user_id)

@users_bp.route("/users/<int:user_id>/favorites/<int:recipe_id>", methods=["DELETE"])
def delete_favorite(user_id, recipe_id):
    return 'favorite deleted! ' + str(recipe_id)