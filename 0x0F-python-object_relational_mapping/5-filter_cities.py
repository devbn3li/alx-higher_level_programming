#!/usr/bin/python3
"""Script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    mydb = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )
    cur = mydb.cursor()

    query = """SELECT cities.name FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s ORDER BY cities.id ASC"""
    cur.execute(query, (argv[4],))

    res = cur.fetchall()
    print(", ".join([row[0] for row in res]))
    cur.close()
    mydb.close()
