#!/usr/bin/python3
'''script that lists all cities from the database
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import State, Base

if __name__ == '__main__':

    username = argv[1]
    password = argv[2]
    database = argv[3]

    db_connection = create_engine("mysql+mysqldb://{:s}:{:s}@localhost/{:s}"
                                  .format(username, password, database))

    Base.metadata.create_all(db_connection)
    session_basedata = sessionmaker(bind=db_connection)
    init_basedata = session_basedata()
    query = init_basedata.query(State).first()

    if not query:
        print("Nothing")
    else:
        print("{}: {}".format(query.id, query.name))

    init_basedata.close()
