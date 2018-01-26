#!/usr/bin/python

json_string = '{"user": "cop4331", "password": ""}'

# Parse json
import json
parsed_json = json.loads(json_string)

# Connect to the database.
import pymysql

conn = pymysql.connect(
    host='localhost',
    db='example',
    user=parsed_json['user'],
    password=parsed_json['password'],
    defer_connect=True
)

try:
    conn.begin()

    with conn.cursor() as cursor:
        #
        sql = "SELECT `id`, `user`, `passwd` FROM users"
        cursor.execute(sql)
        result = cursor.fetchone()
        print (result)

except:
    print ("Error!")
finally:
    conn.close()
