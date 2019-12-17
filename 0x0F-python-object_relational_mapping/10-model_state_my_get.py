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
    search = argv[4]

    db_connection = create_engine("mysql+mysqldb://{:s}:{:s}@localhost/{:s}"
                                  .format(username, password, database))

    Base.metadata.create_all(db_connection)
    session_basedata = sessionmaker(bind=db_connection)
    init_basedata = session_basedata()
    query = session_basedata().query(State).filter(State.name.like(
                                                    argv[4])).all()

    if not query:
        print("Not found")
    else:
        print("{}".format(query[0].id))

    init_basedata.close()
