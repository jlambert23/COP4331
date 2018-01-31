#!/usr/bin/python3
# coding: utf-8

import json
print("Content-Type: application/json\n\n")

def getjson():
    import sys
    return json.load(sys.stdin)

def sendjson(message):
    print(json.dumps(message))

def throwErr(message):
    sendjson('{"error":"%s"}' % message)

def login(json):
    import pymysql

    try:
        user = json['username']
        password = json['password']
    except:
        throwErr("JSON incorrectly configured.\n" + str(json))
        return

    try:
        # Import connection settings.
        from dbsettings import connection_properties
        conn = pymysql.connect( **connection_properties )
        cursor = conn.cursor()
    except:
        throwErr("Server was unable to be reached.")
        return

    try:
        # Throw before accessing database if non-alphanumeric characters are used.
        import re
        if not re.match('^[\w-]+$', user) is not None:
            raise Exception
            
        sql = "SELECT id FROM user WHERE username='%s' AND password='%s';" % (user, password)
        cursor.execute(sql)
        
        userid = cursor.fetchone()[0]
        
        sql2 = "SELECT * FROM `contact` WHERE userid='%d';" % userid
        cursor.execute(sql2)
        
        columns = cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
		
        if not result:
            raise Exception
        
        sendjson(result[0])
        conn.close()
        
    except Exception as e:
        throwErr(str(e) + "\nIncorrect login information.")
        return

parsed_json = getjson()
#parsed_json = json.loads('{"username":"user", "password":"password"}')
login(parsed_json)
