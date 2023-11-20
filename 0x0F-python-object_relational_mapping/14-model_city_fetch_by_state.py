#!/usr/bin/python3
"""
 a script prints all City objects from the database hbtn_0e_14_usa:

"""

import sys
from model_city import Base, City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(City, State).order_by(City.id).filter(
        City.state_id == State.id).all()

    for row in result:
        print("{}: ({}) {}".format(row.State.name, row.City.id, row.City.name))
