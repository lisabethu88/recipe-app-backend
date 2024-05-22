from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())


    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "created_at": self.created_at,
            "password": self.password
        }

    @classmethod
    def from_dict(cls, board_data):
        new_user = User(
            id=board_data["id"],
            username=board_data["username"],
            email=board_data["email"],
            created_at=board_data["created_at"],
            password=board_data["password"]   
        )
        return new_user