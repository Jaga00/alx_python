# a script that prints the first State object from the database 

#!/usr/bin/env python3
"""
Module: 7-model_state_fetch_first

Script that prints the first State object from a MySQL database.

Usage:
$ ./7-model_state_fetch_first.py <mysql_username> <mysql_password> <database_name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def fetch_first_state(mysql_username, mysql_password, database_name):
    """
    Prints the first State object from the specified MySQL database.

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

    # Query to fetch the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Display the retrieved State object or "Nothing"
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./7-model_state_fetch_first.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    fetch_first_state(mysql_username, mysql_password, database_name)