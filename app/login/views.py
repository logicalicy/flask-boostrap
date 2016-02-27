from flask import Blueprint, request, redirect, render_template, url_for, flash
from flask.views import MethodView
from flask.ext.login import login_user, logout_user, login_required
from .forms import LoginForm
from .models import User


login = Blueprint('login', __name__, template_folder='templates')


class LoginView(MethodView):

    def get(self):
        form = LoginForm()
        return render_template('login/login.html', title='login', form=form)

    def post(self):
        form = LoginForm()
        if form.validate_on_submit():
            user = User.objects.get_or_404(username=form.username.data)
            if user and User.validate_login(user.password, form.password.data):
                login_user(user)
                flash("Logged in successfully!", category='success')
                return redirect(request.args.get("next") or url_for("posts.list"))
            flash("Wrong username or password!", category='error')
        return render_template('login/login.html', title='login', form=form)


class LogoutView(MethodView):

    def get(self):
        logout_user()
        return redirect(url_for('login.login'))


# Register the urls
login.add_url_rule('/', endpoint='login', view_func=LoginView.as_view('login'))
login.add_url_rule('/logout', view_func=LogoutView.as_view('logout'))
