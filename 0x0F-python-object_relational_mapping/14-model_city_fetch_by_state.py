#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""
from model_city import City
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()
    Base.metadata.create_all(engine)

    cities = session.query(State, City).join(City).order_by(City.id)
    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
