from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from config import DATABASE_URI

Base = declarative_base()  # We need to inherit Base in order to register user with SQAlchemy
engine = create_engine(DATABASE_URI)  # engine now gives SQAlchemy the power to create tables


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)

    def __repr__(self):
        return "<User(id='{}', name='{}', surname='{}')>"\
            .format(self.id, self.name, self.surname)


Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)
