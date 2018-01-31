#!/usr/bin/python3
# coding: utf-8

import util
print("Content-Type: application/json\n\n")
    
def login(jsonPayload):
    import pymysql

    try:
        username = jsonPayload['username']
        password = jsonPayload['password']
    except:
        util.throwErr("JSON incorrectly configured.\n" + str(jsonPayload))
        return

    try:
        # Import connection settings.
        from dbsettings import connection_properties
        conn = pymysql.connect( **connection_properties )
        cursor = conn.cursor()
    except:
        util.throwErr("Server was unable to be reached.")
        return

    try:
        # Throw before accessing database if non-alphanumeric characters are used.
        import re
        if not re.match('^[\w-]+$', username) is not None:
            raise Exception
        
        # Confirm login and retrieve user's information.
        sql = "SELECT firstname, lastname, email, id FROM user WHERE username='%s' AND password='%s';" % (username, password)
        cursor.execute(sql)
        user = cursor.fetchone()
		
        if not user:
            raise Exception
        
        # Obtain contacts owned by current user.
        sql2 = "SELECT * FROM `contact` WHERE userid='%d';" % user[3]
        cursor.execute(sql2)        
        columns = cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
		
        result = [user] + result
        util.sendjson(result)
        conn.close()
        
    except Exception as e:
        util.throwErr(str(e) + "\nIncorrect login information.")
        return

try:
    #import json
    #parsed_json = json.loads('{"username":"user", "password":"password"}')
    parsed_json = util.getjson()
    login(parsed_json)
except:
    util.throwErr("Failed to parse json.")
