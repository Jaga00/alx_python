# a script that lists all cities from the database

#!/usr/bin/env python3
"""
Module: 4-cities_by_state

Script that lists all cities from a MySQL database.

Usage:
$ ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>
"""

import sys
import MySQLdb

def list_cities(mysql_username, mysql_password, database_name):
    """
    Lists all cities from the specified MySQL database.

    Args:
        mysql_username (str): MySQL username.
        mysql_password (str): MySQL password.
        database_name (str): Name of the database to connect to.
    """
    # Establish a connection to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SELECT query to retrieve cities
    cursor.execute("SELECT * FROM cities ORDER BY id ASC")

    # Fetch all rows
    rows = cursor.fetchall()

    # Display the retrieved cities
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    list_cities(mysql_username, mysql_password, database_name)