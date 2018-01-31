#!/usr/bin/python3
# coding: utf-8
import json
print("Content-Type: application/json\n\n")

def getjson():
    import sys
    return json.load(sys.stdin)
	
def throwErr(message):
    print(json.dumps({'error': "" + message + ""}))
    
def add(jsonPayload):
    import pymysql
    
    try:
        firstname = jsonPayload['firstname']
        lastname = jsonPayload['lastname']
        username = jsonPayload['username']
        password = jsonPayload['password']
        email = jsonPayload['email']
    except:
        throwErr("JSON incorrectly configured.\n" + str(jsonPayload))
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
        sql = "INSERT INTO user (firstname,lastname,username,password,email) VALUES ('%s','%s','%s','%s', '%s');" % (firstname, lastname, username, password, email)
        cursor.execute(sql)
        conn.commit()
        
        sql2 = "SELECT * FROM user WHERE username='%s' AND password='%s';" % (username, password)
        cursor.execute(sql2)
        columns = cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
		
        print(json.dumps(result))
        conn.close()
        
    except Exception as e:
        throwErr(str(e) + "\nIncorrect login information.")
        return
        
parsed_json = json.loads('{"username":"babby", "password":"admin", "firstname":"How is", "lastname":"babby formed?", "email":"idontknow@yahoomugs.com"}')
#parsed_json = getjson()
add(parsed_json)
