#!/usr/bin/python3
"""
Script that takes in an arg and displays all values equal to arg in the states
table of htbn_0e_0_usa
"""
import MySQLdb
import sys


def call_query(user, passwd, db, arg):
    """
    calls a query to a specified db

    Args:
        user (str): username
        passwd (str): password
        db (str): db to connect to
        arg (str): argument to pass into query
    """
    conn = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=passwd,
        db=db
        )
    c = conn.cursor()
    c.execute('SELECT * FROM states WHERE name LIKE BINARY {} ORDER BY id ASC'
              .format(arg))
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)
    c.close()
    conn.close()


if __name__ == "__main__":
    call_query(*sys.argv[1:5])
