from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "my_tumble_log"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from app.login.views import login
    from app.posts.views import posts
    from app.admin.views import admin
    app.register_blueprint(login)
    app.register_blueprint(posts)
    app.register_blueprint(admin)

register_blueprints(app)

if __name__ == '__main__':
    app.run()