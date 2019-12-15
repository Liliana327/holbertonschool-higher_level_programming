#!/usr/bin/python3

import MySQLdb
from sys import argv


if __name__ == '__main__':

    '''script that lists all states from the database.'''

    username = argv[1]
    password = argv[2]
    database = argv[3]

    db_connection = MySQLdb.connect(
            host='localhost',
            port= 3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )

    curs = db_connection.cursor()
    curs.execute("SELECT * FROM states ORDER states.id ASC")
    for row in curs.fetchall():
        print(row)
    curs.close()
    db_connection.close()
