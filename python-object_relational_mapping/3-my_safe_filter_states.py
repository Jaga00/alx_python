# one that is safe from MySQL injections!

#!/usr/bin/env python3
"""
Module: 3-my_safe_filter_states

Script that displays all values in the states table where
name matches a given argument from a MySQL database.
Safe from SQL injection.

Usage:
$ ./3-my_safe_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>
"""

import sys
import MySQLdb

def safe_filter_states_by_name(mysql_username, mysql_password, database_name, state_name):
    """
    Display all values in the states table where name matches
    the provided state name argument from the specified MySQL database.
    Safe from SQL injection.

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

    # Create a parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

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
        print("Usage: ./3-my_safe_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    safe_filter_states_by_name(mysql_username, mysql_password, database_name, state_name)