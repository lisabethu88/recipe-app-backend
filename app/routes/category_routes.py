from flask import Blueprint

categories_bp = Blueprint("categories", __name__)
@categories_bp.route("/categories", methods=["GET"])
def get_all_categories():
    return 'categories'

@categories_bp.route("/categories/<int:category_id>/recipes", methods=["GET"])
def get_recipes_by_category(category_id):
    return 'recipes by category ' + str(category_id)