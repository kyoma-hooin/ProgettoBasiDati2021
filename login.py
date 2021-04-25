from flask import render_template
from flask import Blueprint

login_bp = Blueprint('login_bp', __name__)


@login_bp.route('/users/<username>')
def show_profile(username):
    users = ['bob', 'alice']
    if username in users:
        return render_template('profile.html', user=username)
    return render_template('profile.html', reg=users)
