from flask import Blueprint

recipes_bp = Blueprint("recipes", __name__)
@recipes_bp.route("/recipes", methods=["GET"])
def get_all_recipes():
    return 'recipes'

@recipes_bp.route("/recipes/<int:recipe_id>", methods=["GET"])
def get_recipe_by_id(recipe_id):
    return {"recipe_id":  recipe_id}

@recipes_bp.route("/recipes", methods=["POST"])
def create_recipe():
    return 'recipe created!'

@recipes_bp.route("/recipes/<int:recipe_id>", methods=["PUT"])
def update_recipe(recipe_id):
    return 'recipe updated! ' + str(recipe_id)

@recipes_bp.route("/recipes/<int:recipe_id>", methods=["DELETE"])
def delete_recipe(recipe_id):
    return 'recipe deleted! ' + str(recipe_id)

# ingredients routes
@recipes_bp.route("/recipes/<int:recipe_id>/ingredients", methods=["GET"])
def get_all_ingredients():
    return 'ingredients'

@recipes_bp.route("/recipes/<int:recipe_id>/ingredients/<int:ingredient_id>", methods=["PUT"])
def update_ingredient(recipe_id, ingredient_id):
    return 'ingredient updated! ' + str(ingredient_id)

@recipes_bp.route("/recipes/<int:recipe_id>/ingredients/<int:ingredient_id>", methods=["DELETE"])
def delete_ingredient(recipe_id, ingredient_id):
    return 'ingredient deleted! ' + str(ingredient_id)

# step routes
@recipes_bp.route("/recipes/<int:recipe_id>/steps", methods=["GET"])
def get_all_steps(recipe_id):
    return 'steps' + str(recipe_id)

@recipes_bp.route("/recipes/<int:recipe_id>/steps", methods=["POST"])
def create_step(recipe_id):
    return 'step created! ' + str(recipe_id)

@recipes_bp.route("/recipes/<int:recipe_id>/steps/<int:step_id>", methods=["PUT"])
def update_step(recipe_id, step_id):
    return 'step updated! ' + str(step_id)

@recipes_bp.route("/recipes/<int:recipe_id>/steps/<int:step_id>", methods=["DELETE"])
def delete_step(recipe_id, step_id):
    return 'step deleted! ' + str(step_id)