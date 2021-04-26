from flask import render_template
from flask import Blueprint

profile_bp = Blueprint('profile_bp', __name__)


@profile_bp.route('/users/<username>')
def show_profile(username):
    users = ['Leonardo', 'Giacomo', 'Simone']
    if username in users:
        return render_template('profile.html', user=username)
    return render_template('profile.html')
