from flask import Flask
from sqlalchemy import create_engine
from models import Base

app = Flask(__name__)
DATABASE_URI = 'postgresql+psycopg2://postgres:progetto2021@localhost:5432/palestre'
engine = create_engine(DATABASE_URI)  # 'sqlite:///C:\\Università\\Secondo Anno\\Basi di Dati\\Modulo
# 2\\Progetto\\database.db'


@app.route('/')
def hello_world():
    Base.metadata.create_all(engine)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
