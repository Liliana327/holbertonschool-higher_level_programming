#!/usr/bin/python3
'''script takes in argument and displays all values in the states
'''
import MySQLdb
from sys import argv

if __name__ == '__main__':

    username = argv[1]
    password = argv[2]
    database = argv[3]
    searched = argv[4]

    db_connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
        )

    curs = db_connection.cursor()
    curs.execute("SELECT * FROM states WHERE name='{}'"
                 .format(searched))

    for row in curs.fetchall():
        print(row)
    curs.close()
    db_connection.close()
