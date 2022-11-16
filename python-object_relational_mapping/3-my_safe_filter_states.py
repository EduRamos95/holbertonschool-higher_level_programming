#!/usr/bin/python3
"""List all states using mysqldb"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    cmd_database = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cur.execute(cmd_database, (argv[4],))
    for row in cur.fetchall():
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()
