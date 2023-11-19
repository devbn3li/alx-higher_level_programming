#!/usr/bin/python3
"""Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=argv[1], passwd=argv[2], db=argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%';")

    states = cur.fetchall()
    for state in states:
        print(state)
