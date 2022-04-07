#!/usr/bin/env python3
import MySQLdb
from sys import argv

try:
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
            )
    cur = db.cursor()
except Exception as ex:
    print(ex)

try:
    query = f'''select c.name from states as s
            left join cities as c
            on c.state_id = s.id
            where s.name = %s'''

    cur.execute(query, (argv[4],))
    query_rows = cur.fetchall()

    res = ''
    for idx in range(len(query_rows) - 1):
        row = query_rows[idx]
        row = str(row).strip("('")
        row = row.strip("',)")
        if idx != 0:
            res += (', ' + row)
        else:
            res += (row)
    print(res)

    cur.close()
    db.close()
except Exception as ex:
    print(ex)