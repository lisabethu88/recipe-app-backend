from app import db

class Step(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    step_number = db.Column(db.Integer, nullable=False)
    instruction = db.Column(db.Text, nullable=False)
    recipe = db.relationship('Recipe', backref=db.backref('steps', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "recipe_id": self.recipe_id,
            "step_number": self.step_number,
            "instruction": self.instruction,
            "recipe": self.recipe.to_dict()
        }

    @classmethod
    def from_dict(cls, step_data):
        new_step = Step(
            id=step_data["id"],
            recipe_id=step_data["recipe_id"],
            step_number=step_data["step_number"],
            instruction=step_data["instruction"],
            recipe=step_data["recipe"]
        )
        return new_step