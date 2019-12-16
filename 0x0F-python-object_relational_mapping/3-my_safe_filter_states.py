#!/usr/bin/python3
'''is an SQL injection to delete all records of a table
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
    curs.execute("SELECT * FROM states WHERE name=%s \
                  ORDER BY states.id ASC", (searched,))

    for row in curs.fetchall():
        print(row)
    curs.close()
    db_connection.close()
