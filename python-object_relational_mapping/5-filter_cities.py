#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost",  port=3306,
                         user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3])

    cursor = db.cursor()
    stateName = sys.argv[4]
    cursor.execute("SELECT c.name "
                   "FROM cities AS c "
                   "INNER JOIN states AS s "
                   "ON c.state_id=s.id WHERE BINARY s.name "
                   "= BINARY %s ORDER BY c.id ASC", (stateName,))
    lists = []
    query_rows = cursor.fetchall()
    for row in query_rows:
        lists.append(row[0])
    print(", ".join(lists))
    cursor.close()
    db.close()
