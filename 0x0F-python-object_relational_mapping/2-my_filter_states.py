#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument
Connects to a MySQL server running on localhost at port 3306
Results are sorted in ascending order by states.id
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    db.close()
