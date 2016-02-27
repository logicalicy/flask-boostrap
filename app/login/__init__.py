from flask import redirect, url_for
from app import login_manager
from .models import User

@login_manager.user_loader
def load_user(username):
    """
    Reloads user object from the user ID stored in the session.
    A user loader must be installed with a `LoginManager`.
    """
    user = User.objects.get_or_404(username=username)
    if not user:
        return None
    return user

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login.login'))