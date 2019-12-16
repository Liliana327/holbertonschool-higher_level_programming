#!/usr/bin/python3
'''script that lists all cities from the database
'''
import MySQLdb
from sys import argv

if __name__ == '__main__':

    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    db_connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
        )

    curs = db_connection.cursor()
    curs.execute("SELECT cities.name FROM cities JOIN states ON states.id\
                 = cities.state_id WHERE states.name=%s\
                 ORDER BY states.id ASC", (state_name,))
    empty_list = []
    for row in curs.fetchall():
        empty_list.append(row[0])
    print(", ".join(empty_list))
    curs.close()
    db_connection.close()
