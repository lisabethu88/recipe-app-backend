from flask import Flask
from .routes.user_routes import users_bp
from .routes.recipe_routes import recipes_bp
from .routes.category_routes import categories_bp

def create_app(test_config=None):
    app = Flask(__name__)
    app.register_blueprint(recipes_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(categories_bp)

    return app