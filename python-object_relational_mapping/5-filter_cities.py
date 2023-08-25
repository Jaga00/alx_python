# a script that takes in the name of a state as an argument and lists all cities of that state

#!/usr/bin/env python3
"""
Module: 5-filter_cities

Script that lists all cities of a given state from a MySQL database.

Usage:
$ ./5-filter_cities.py <mysql_username> <mysql_password> <database_name> <state_name>
"""

import sys
import MySQLdb

def filter_cities_by_state(mysql_username, mysql_password, database_name, state_name):
    """
    Lists all cities of a given state from the specified MySQL database.

    Args:
        mysql_username (str): MySQL username.
        mysql_password (str): MySQL password.
        database_name (str): Name of the database to connect to.
        state_name (str): Name of the state to filter by.
    """
    # Establish a connection to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Create a parameterized query to prevent SQL injection
    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all rows
    rows = cursor.fetchall()

    # Display the retrieved cities
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <mysql_username> <mysql_password> <database_name> <state_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    filter_cities_by_state(mysql_username, mysql_password, database_name, state_name)