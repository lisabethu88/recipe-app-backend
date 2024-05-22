from app import db

class RecipeIngredient(db.Model):
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), primary_key=True)
    quantity = db.Column(db.String(50))
    recipe = db.relationship('Recipe', backref=db.backref('recipe_ingredients', lazy=True))
    ingredient = db.relationship('Ingredient', backref=db.backref('recipe_ingredients', lazy=True))

    def to_dict(self):
        return {
            "recipe_id": self.recipe_id,
            "ingredient_id": self.ingredient_id,
            "quantity": self.quantity,
            "recipe": self.recipe.to_dict(),
            "ingredient": self.ingredient.to_dict()
        }

    @classmethod
    def from_dict(cls, recipe_ingredient_data):
        new_recipe_ingredient = RecipeIngredient(
            recipe_id=recipe_ingredient_data["recipe_id"],
            ingredient_id=recipe_ingredient_data["ingredient_id"],
            quantity=recipe_ingredient_data["quantity"],
            recipe=recipe_ingredient_data["recipe"],
            ingredient=recipe_ingredient_data["ingredient"]
        )
        return new_recipe_ingredient