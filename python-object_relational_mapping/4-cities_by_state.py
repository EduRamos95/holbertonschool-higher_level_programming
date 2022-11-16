#!/usr/bin/python3
""" Script that lists all cities from
    the database hbtn_0e_4_usa.
"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost",  port=3306,
                         user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3])

    cursor = db.cursor()
    cmd_db = """SELECT cities.id, cities.name, states.name
            FROM cities JOIN states
            ON cities.state_id = states.id
            ORDER BY id ASC"""
    cursor.execute(cmd_db)
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    db.close()
