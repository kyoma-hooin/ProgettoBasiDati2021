from flask import Flask
from login import login_bp
from profile import profile_bp
import views

app = Flask(__name__)  # represents our application
app.register_blueprint(profile_bp)  # when a Flask Blueprint is registered the application is extended with its contents
app.register_blueprint(login_bp)
app.register_blueprint(views.bp)


if __name__ == '__main__':

    app.run(debug=True)
