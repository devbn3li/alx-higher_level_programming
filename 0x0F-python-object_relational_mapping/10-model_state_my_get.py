#!/usr/bin/python3
"""script that prints the State object with the name passed as argument from
the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    if len(sys.argv) == 5:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                               format(sys.argv[1], sys.argv[2], sys.argv[3]),
                               pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).filter(
            State.name == sys.argv[4]).first()

        if state:
            print("{}".format(state.id))
        else:
            print("Not found")
    else:
        print("Usage: mysql_username mysql_password database_name state_name")
