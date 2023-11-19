#!/usr/bin/python3
"""list all states from the database hbtn_0e_0_usa"""

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
    mycursor = mydb.cursor()

    query = """SELECT * FROM states WHERE BINARY name
    LIKE 'N%' ORDER BY ID ASC"""
    mycursor.execute(query)

    result = mycursor.fetchall()
    for row in result:
        print(row)
    mycursor.close()
    mydb.close()
