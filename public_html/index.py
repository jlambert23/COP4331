#For use with mysql db "testing".

#!/usr/bin/python

# Turn on debug mode.
import cgitb
cgitb.enable()

# Print necessary headers.
print("Content-Type: text/html")
print()

# Connect to the database.
import pymysql
conn = pymysql.connect( defer_connect=True)
conn.Connect(
    db='example',
    user='db-sys',
    password='',
    host='localhost'
)
c = conn.cursor()

# Insert some example data.
c.execute("INSERT INTO numbers VALUES (1, 'One!')")
c.execute("INSERT INTO numbers VALUES (2, 'Two!')")
c.execute("INSERT INTO numbers VALUES (3, 'Three!')")
conn.commit()

# Print the contents of the database.
c.execute("SELECT * FROM numbers")
print([(r[0], r[1]) for r in c.fetchall()])
