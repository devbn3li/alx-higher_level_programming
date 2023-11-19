#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Engine creation"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    """Session creation"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Query"""
    query = session.query(State).filter(State.name == sys.argv[4]).first()
    if query is None:
        print("Not found")
    else:
        print(query.id)
    session.close()


