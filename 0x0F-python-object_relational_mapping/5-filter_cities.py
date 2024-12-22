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
    """
    conn = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=passwd,
        db=db
        )
    c = conn.cursor()
    c.execute("""
            SELECT
            cities.name
            from cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = '{}'
            """.format(args[3]))
    query_rows = c.fetchall()
    print(", ".join(row[0] for row in query_rows))
    c.close()
    conn.close()


if __name__ == "__main__":
    call_query(*sys.argv[1:5])
