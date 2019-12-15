#!/usr/bin/python3
import MySQLdb
from sys import argv


def mysqlconnect():

    db_connection = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db_connection.close()

mysqlconnect()
