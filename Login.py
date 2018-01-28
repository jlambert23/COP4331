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
#sql = "SELECT `id`, `user`, `passwd` FROM users"
sql = "SELECT id FROM users WHERE passwd='9ed1515819dec61fd361d5fdabb57f41ecce1a5fe1fe263b98c0d6943b9b232e'"
cursor.execute(sql)
result = cursor.fetchone()
print (result)

conn.close()
