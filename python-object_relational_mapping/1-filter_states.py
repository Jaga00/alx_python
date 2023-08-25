#  a script that lists all states with a name starting with N (upper N)

#!/usr/bin/env python3
"""
Module: 1-filter_states

Script that lists all states with names starting with 'N' (uppercase)
from a MySQL database.

Usage:
$ ./1-filter_states.py <mysql_username> <mysql_password> <database_name>
"""

import sys
import MySQLdb

def filter_states(mysql_username, mysql_password, database_name):
    """
    Retrieve and list all states with names starting with 'N' (uppercase)
    from the specified MySQL database.

    Args:
        mysql_username (str): MySQL username.
        mysql_password (str): MySQL password.
        database_name (str): Name of the database to connect to.
    """
    # Establish a connection to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SELECT query to retrieve filtered states
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows
    rows = cursor.fetchall()

    # Display the retrieved states
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./1-filter_states.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    filter_states(mysql_username, mysql_password, database_name)