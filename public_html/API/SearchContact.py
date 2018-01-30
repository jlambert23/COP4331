#!/usr/bin/python
# coding: utf-8

def searchcontact(json):
    import pymysql

    try:
        name = json['name']
        #phone = json['phone']
        #email = json['email']
        user_id = json['userID']

        # Import connection settings.
        from dbsettings import connection_properties
        conn = pymysql.connect( **connection_properties )
        cursor = conn.cursor()

        # Check if contact already exists.
        sql = "SELECT * FROM contact WHERE name='%s' AND userID=%d" % (name, user_id)
        cursor.execute(sql)
        result = cursor.fetchone()
        conn.close()

        return result

    except Exception as e:
        sendjson("Unable to find contact.\n" + str(e))

def getjson():
    import sys
    return json.load(sys.stdin)

def sendjson(message):
    header = "Content-type: application/json\n\n"
    print(header + json.dumps(message))

import json
#parsed_json = getjson()

# -- Testing --
json_string = '{"name": "Johnny", "phone":"123-456-7890", "email":"computers@nerds.org", "userID":1}'
parsed_json = json.loads(json_string)

if searchcontact(parsed_json):
    print(parsed_json['name'] + " was found in your contacts.")

