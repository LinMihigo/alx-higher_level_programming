#!/usr/bin/python3
"""
Script that takes in an arg and displays all values equal to arg in the states
table of htbn_0e_0_usa

Attributes:
    args (list): list of arguments received from cli
    conn (mysql.connector.connection.MySQLConnection): object repr-
        esenting a connection to MySQL db
    c (mysql.connector.cursor.MySQLCursor): cursor object
    query_rows (list): list of tuples holding the query results
"""
import MySQLdb
import sys


args = sys.argv[1:5]

conn = MySQLdb.connect(
    host="localhost",
    user=args[0],
    passwd=args[1],
    db=args[2]
    )
c = conn.cursor()
c.execute('SELECT * FROM states WHERE name = "{}" ORDER BY id ASC'
          .format(args[3]))
query_rows = c.fetchall()
for row in query_rows:
    print(row)
c.close()
conn.close()
