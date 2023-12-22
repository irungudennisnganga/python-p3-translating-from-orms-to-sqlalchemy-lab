from models import Dog
import os
import ipdb;
# from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# engine = create_engine('sqlite:///lib/dogs.db')
base = declarative_base()

def create_table(base,engine):
    
    base.metadata.create_all(engine)

    
def save(session, dog):
    session.add(dog)
    

def get_all(session):
    return session.query(Dog)
    # session.commit()

def find_by_name(session, name):
    return session.query(Dog).filter_by(name = name).first()
    # print(new)

def find_by_id(session, id):
    return session.query(Dog).filter_by(id = id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter_by(name = name,breed = breed).first()

def update_breed(session, dog, breed):
    # return session.query(Dog).update({dog.breed:dog.breed})
    dog.breed = breed
    session.commit()

# ipdb.set_trace()