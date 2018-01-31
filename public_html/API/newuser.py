#!/usr/bin/python3
# coding: utf-8

import util
print("Content-Type: application/json\n\n")
    
def newuser(jsonPayload):
    import pymysql
    
    try:
        firstname = jsonPayload['firstname']
        lastname = jsonPayload['lastname']
        username = jsonPayload['username']
        password = jsonPayload['password']
        email = jsonPayload['email']
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
        try:
            # Throw before accessing database if non-alphanumeric characters are used.
            import re
            if not re.match('^[\w-]+$', username) is not None:
                raise Exception
            
            # Insert new user into the database.
            sql = "INSERT INTO user (firstname,lastname,username,password,email) VALUES ('%s','%s','%s','%s', '%s');" % (firstname, lastname, username, password, email)
            cursor.execute(sql)
            conn.commit()
        except:
            util.throwErr("User name already in use.")
    
        # Retrieve user information.
        sql2 = "SELECT * FROM user WHERE username='%s' AND password='%s';" % (username, password)
        cursor.execute(sql2)
        columns = cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
		
        util.sendjson(result)
        conn.close()
        
    except:
        util.throwErr("Unable to create new user.")
        return
   
try:
    #import json
    #parsed_json = json.loads('{"username":"babby", "password":"admin", "firstname":"How is", "lastname":"babby formed?", "email":"idontknow@yahoomugs.com"}')
    parsed_json = util.getjson()
    newuser(parsed_json)
except:
    util.throwErr("Failed to parse json.")
