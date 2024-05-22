from app import db

class Favorite(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), primary_key=True)
    user = db.relationship('User', backref=db.backref('favorites', lazy=True))
    recipe = db.relationship('Recipe', backref=db.backref('favorites', lazy=True))

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "recipe_id": self.recipe_id,
            "user": self.user.to_dict(),
            "recipe": self.recipe.to_dict()
        }

    @classmethod
    def from_dict(cls, favorite_data):
        new_favorite = Favorite(
            user_id=favorite_data["user_id"],
            recipe_id=favorite_data["recipe_id"],
            user=favorite_data["user"],
            recipe=favorite_data["recipe"]
        )
        return new_favorite