from flask import Blueprint, request, redirect, url_for

login_bp = Blueprint('login_bp', __name__)


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    user = request.form["user"]
    return redirect(url_for('profile_bp.show_profile', username=user))
