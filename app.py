from flask import Flask, render_template
from login import login_bp

app = Flask(__name__)
app.register_blueprint(login_bp)  # when a Flask Blueprint is registered, the application is extended with its contents


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
