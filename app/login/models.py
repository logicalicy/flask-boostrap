import datetime
from werkzeug.security import check_password_hash
from app import db

class User(db.Document):

    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    username = db.StringField(verbose_name="Username", required=True)
    password = db.StringField(verbose_name="Password", max_length=255, required=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)