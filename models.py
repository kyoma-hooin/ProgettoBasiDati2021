from sqlalchemy import Column, create_engine, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URI

Base = declarative_base()
engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'Users'
    codicefiscale = Column(String, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    password = Column(String)

    def __init__(self, name, surname, codicefiscale, email, password):
        self.surname = surname
        self.name = name
        self.codicefiscale = codicefiscale
        self.email = email
        self.password = password


def create_user(name, surname, codicefiscale, email, password):
    user = User(name, surname, codicefiscale, email, password)
    session.add(user)
    session.commit()

    return user


if __name__ == '__main__':
    # Base.metadata.create_all(engine)

    for namen, surnamen, codicefiscalen, emailn, passwordn in session.query(User.name, User.surname, User.codicefiscale, User.email, User.password):
        print(namen, surnamen, codicefiscalen, emailn, passwordn)
