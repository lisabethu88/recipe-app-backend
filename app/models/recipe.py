from app import db


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    user = db.relationship('User', backref=db.backref('recipes', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "description": self.description,
            "title": self.title,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "user": self.user.to_dict()
        }

    @classmethod
    def from_dict(cls, recipe_data):
        new_recipe = Recipe(
            id=recipe_data["id"],
            user_id=recipe_data["user_id"],
            description=recipe_data["description"],
            title=recipe_data["title"],
            created_at=recipe_data["created_at"],
            updated_at=recipe_data["updated_at"],
            user=recipe_data["user"]  
        )
        return new_recipe