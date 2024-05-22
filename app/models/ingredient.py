from app import db

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def from_dict(cls, ingredient_data):
        new_ingredient = Ingredient(
            id=ingredient_data["id"],
            name=ingredient_data["name"]   
        )
        return new_ingredient