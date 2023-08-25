# a script that takes in an argument and displays all values in the states table

#!/usr/bin/env python3
"""
Module: 2-my_filter_states

Script that displays all values in the states table where
name matches a given argument from a MySQL database.

Usage:
$ ./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>
"""

import sys
import MySQLdb

def filter_states_by_name(mysql_username, mysql_password, database_name, state_name):
    """
    Display all values in the states table where name matches
    the provided state name argument from the specified MySQL database.

    Args:
        mysql_username (str): MySQL username.
        mysql_password (str): MySQL password.
        database_name (str): Name of the database to connect to.
        state_name (str): State name to search for.
    """
    # Establish a connection to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Create and execute the SQL query with user input using format
    query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Display the retrieved states
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    filter_states_by_name(mysql_username, mysql_password, database_name, state_name)