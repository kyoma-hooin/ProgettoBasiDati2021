from flask import Flask, render_template
from login import login_bp
from profile import profile_bp

app = Flask(__name__)  # represents our application
app.register_blueprint(profile_bp)  # when a Flask Blueprint is registered the application is extended with its contents
app.register_blueprint(login_bp)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
