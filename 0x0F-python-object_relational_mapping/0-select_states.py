#!/usr/bin/python3
"""
Script that lists all states from a db - htbn_0e_0_usa
"""
import MySQLdb
import sys


def call_query(user, passwd, db):
    """
    calls a query to a specified db

    Args:
        user (str): username
        passwd (str): password
        db (str): db to connect to
    """
    conn = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=passwd,
        db=db
        )
    c = conn.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)
    c.close()
    conn.close()


if __name__ == "__main__":
    call_query(*sys.argv[1:4])
