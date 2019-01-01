from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship


Base = declarative_base()

class User(Base):
    __tablename__ = "person"

    id = Column('id',Integer,primary_key=True)
    username = Column('username',String,unique=True)

engine = create_engine('sqlite:///newbey',echo=True)
connection = engine.connect()

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
user = User()
user.id = 1
user.username = 'bob'

session.add(user)
session.commit()

session.close()
