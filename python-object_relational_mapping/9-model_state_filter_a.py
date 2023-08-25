#a script that lists all State objects that contain the letter a from the database

#!/usr/bin/env python3
"""
Module: 8-model_state_fetch_filter

Script that lists all State objects containing the letter "a" from a MySQL database.

Usage:
$ ./8-model_state_fetch_filter.py <mysql_username> <mysql_password> <database_name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def fetch_filtered_states(mysql_username, mysql_password, database_name):
    """
    Lists all State objects containing the letter "a"
    from the specified MySQL database.

    Args:
        mysql_username (str): MySQL username.
        mysql_password (str): MySQL password.
        database_name (str): Name of the database to connect to.
    """
    # Create a connection to the MySQL database
    engine = create_engine(f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}")

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to fetch filtered State objects and order by id
    filtered_states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Display the retrieved State objects
    for state in filtered_states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./8-model_state_fetch_filter.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    fetch_filtered_states(mysql_username, mysql_password, database_name)