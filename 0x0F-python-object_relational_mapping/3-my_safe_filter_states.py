#!/usr/bin/python3
"""
Script that lists all states from a db - htbn_0e_0_usa

Attributes:
    args (list): list of arguments received from cli
    conn (mysql.connector.connection.MySQLConnection): object repr-
        esenting a connection to MySQL db
    c (mysql.connector.cursor.MySQLCursor): cursor object
    query_rows (list): list of tuples holding the query results
"""
import MySQLdb
import sys
import re


args = sys.argv[1:5]


def validator(arg):
    """
    Checks if arg meets specific criteria (only alphanumeric)

    Args:
        arg (str): string to check

    Returns:
        bool: true if successful, false otherwise
    """
    return bool(re.match(r'^[a-zA-Z0-9]+$', arg))


conn = MySQLdb.connect(
    host="localhost",
    user=args[0],
    passwd=args[1],
    db=args[2]
    )
c = conn.cursor()

if not validator(args[3]):
    raise ValueError("Invalid argument")

c.execute('SELECT * FROM states WHERE name = "{}" ORDER BY id ASC'
          .format(args[3]))
query_rows = c.fetchall()
for row in query_rows:
    print(row)
c.close()
conn.close()
