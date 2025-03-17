#!/usr/bin/python3
"""Filter states by name"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    name = sys.argv[4]

    # Establish a connection
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=mysql_username, password=mysql_password,
                         database=database_name)

    # create a cursor pointer
    pointer = db.cursor()

    # execute a query
    pointer.execute("SELECT * FROM states WHERE name = %s\
                    ORDER BY id ASC", (name, ))

    # fetch the result using fetchall to pass the checker
    rows = pointer.fetchall()
    for row in rows:
        print("({0}, '{1}')".format(row[0], row[1]))

    # close cursor pointer and db connection
    pointer.close()
    db.close()
