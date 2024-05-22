from app import db

class RecipeCategory(db.Model):
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), primary_key=True)
    recipe = db.relationship('Recipe', backref=db.backref('recipe_categories', lazy=True))
    category = db.relationship('Category', backref=db.backref('recipe_categories', lazy=True))

    def to_dict(self):
        return {
            "recipe_id": self.recipe_id,
            "category_id": self.category_id,
            "recipe": self.recipe.to_dict(),
            "category": self.category.to_dict()
        }

    @classmethod
    def from_dict(cls, recipe_category_data):
        new_recipe_category = RecipeCategory(
            recipe_id=recipe_category_data["recipe_id"],
            category_id=recipe_category_data["category_id"],
            recipe=recipe_category_data["recipe"],
            category=recipe_category_data["category"]
        )
        return new_recipe_category