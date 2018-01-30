#!/usr/bin/python

def login(json):
    import pymysql

    try:
        user = json['userName']
        passwd = json['password']

        # Import connection settings.
        from dbsettings import connection_properties
        conn = pymysql.connect( **connection_properties )
        cursor = conn.cursor()

        # Lookup user.
        try:
            sql = "SELECT * FROM user WHERE userName='%s' AND password='%s';" % (user,passwd)
            cursor.execute(sql)
        except:
            sendjson('{"error":"Incorrect Login information."}')

        result = cursor.fetchone()
        conn.close()

        return result

    except:
        sendjson("Unable to login.")

def getjson():
    import sys
    return json.load(sys.stdin)

def sendjson(message):
    header = "Content-type: application/json\n\n"
    print(header + json.dumps(message))


import json
#parsed_json = getjson()

# -- Testing --
json_string = '{"userName": "user", "password": "password"}'
parsed_json = json.loads(json_string)

message = login(parsed_json)
print(message)
