#!/usr/bin/python

json_string = '{"user": "db-sys", "password": ""}'

# Parse json
import json
parsed_json = json.loads(json_string)

# Connect to the database.
import pymysql

conn = pymysql.connect(
    host='localhost',
    db='jayTest',
    user=parsed_json['user'],
    password=parsed_json['password']
)
cursor = conn.cursor()

# Get some data.
sql = "SELECT `id`, `user`, `passwd` FROM users;"
cursor.execute(sql)
result = cursor.fetchall()
print (result)

conn.close()
