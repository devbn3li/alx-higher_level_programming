#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""

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

    query = """SELECT cities.id, cities.name, states.name FROM cities
    INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"""
    cur.execute(query)

    res = cur.fetchall()
    for row in res:
        print(row)
    cur.close()
    mydb.close()
