from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

app = Flask(__name__)
engine = create_engine('sqlite:///C:\\Università\\Secondo Anno\\Basi di Dati\\Modulo 2\\Progetto\\database.db')
Base = declarative_base()

@app.route('/')
def hello_world():
    Base.metadata.create_all(engine)
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
