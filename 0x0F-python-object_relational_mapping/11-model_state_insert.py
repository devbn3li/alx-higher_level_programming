#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the database 
hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == '__main__':
    if len(sys.argv) == 4:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                               format(sys.argv[1], sys.argv[2], sys.argv[3]),
                               pool_pre_ping=True)

        Base.metadata.create_all(engine)
        conn = engine.connect()
        conn.execute("INSERT INTO states (name) VALUES ('Louisiana')")
        conn.close()
    else:
        print("Usage: mysql_username mysql_password database_name")
