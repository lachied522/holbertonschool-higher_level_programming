#!/usr/bin/python3
"""Get states starting with 'N'"""
import MySQLdb
import sys

if __name__ == "__main__":
    n = len(sys.argv)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Establish a connection
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=mysql_username, password=mysql_password,
                         database=database_name)

    # create a cursor pointer
    pointer = db.cursor()

    # execute a query
    pointer.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%'\
                    ORDER BY id ASC")

    # fetch the result using fetchall to pass the checker
    rows = pointer.fetchall()
    for row in rows:
        print("({0}, '{1}')".format(row[0], row[1]))

    # close cursor pointer and db connection
    pointer.close()
    db.close()
