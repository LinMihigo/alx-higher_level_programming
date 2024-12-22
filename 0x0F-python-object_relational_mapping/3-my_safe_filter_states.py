#!/usr/bin/python3
"""
Script that lists all states from a db - htbn_0e_0_usa
"""
import MySQLdb
import sys
import re


def validator(arg):
    """
    Checks if arg meets specific criteria (only alphanumeric)

    Args:
        arg (str): string to check

    Returns:
        bool: true if successful, false otherwise
    """
    return bool(re.match(r'^[a-zA-Z0-9]+$', arg))


def call_query(user, passwd, db, arg):
    """
    calls a query to a specified db

    Args:
        user (str): username
        passwd (str): password
        db (str): db to connect to
        arg (str): argument to pass to query-
    """
    conn = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=passwd,
        db=db
        )
    c = conn.cursor()

    if not validator(arg):
        raise ValueError("Invalid argument")

    c.execute('SELECT * FROM states WHERE name = "{}" ORDER BY id ASC'
              .format(arg))
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)
    c.close()
    conn.close()


if __name__ == "__main__":
    call_query(*sys.argv[1:5])
