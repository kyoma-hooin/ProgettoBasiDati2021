from flask import render_template, request, Blueprint
from models import create_user

bp = Blueprint('views', __name__, url_prefix='/')


@bp.route('/')
def hello_world():
    return render_template('index.html')


@bp.route('/adduser', methods=['GET', 'POST'])
def add_user():
    if request.method == 'GET':
        return render_template('adduser.html')

    user_name = request.form.get('name')
    user_surname = request.form.get('surname')
    user_codicefiscale = request.form.get('codicefiscale')
    user_email = request.form.get('email')
    user_password = request.form.get('password')

    user = create_user(user_name, user_surname, user_codicefiscale, user_email, user_password)
    return render_template('adduser.html', user=user)
