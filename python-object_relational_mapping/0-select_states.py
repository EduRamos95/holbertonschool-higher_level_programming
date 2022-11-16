#!/usr/bin/python3
"""
return all table values (table 'states')
parameters given to script: username, password, database
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    # connect to database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         database=argv[3])

    # create cursor to exec queries using SQL
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
