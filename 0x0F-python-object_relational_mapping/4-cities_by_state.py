#!/usr/bin/python3
'''script that lists all cities from the database
'''
import MySQLdb
from sys import argv

if __name__ == '__main__':

    username = argv[1]
    password = argv[2]
    database = argv[3]

    db_connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
        )

    curs = db_connection.cursor()
    curs.execute("SELECT cities.id, cities.name, states.name \
                 FROM cities JOIN states ON states.id = cities.state_id"
                 .format(database))
    for row in curs.fetchall():
        print(row)
    curs.close()
    db_connection.close()
