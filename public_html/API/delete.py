#!/usr/bin/python3
# coding: utf-8

import json
print("Content-Type: application/json\n\n")

def getjson():
    import sys
    return json.load(sys.stdin)

def throwErr(message):
    print(json.dumps({'error': "" + message + ""}))
    
def login(jsonPayload):
    import pymysql

    try:
        firstname = jsonPayload['firstname']
        lastname = jsonPayload['lastname']
        phone = jsonPayload['phone']
        email = jsonPayload['email']
        userid = jsonPayload['userid']
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
        sql = "DELETE FROM contact WHERE firstname='%s' AND lastname='%s' AND phone='%s' AND email='%s' AND userid=%d;" % (firstname, lastname, phone, email, userid)
        cursor.execute(sql)        
        conn.commit()
        
        sql2 = "SELECT * FROM `contact` WHERE userid='%d';" % userid
        cursor.execute(sql2)        
        columns = cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
		
        result = [userid] + result
        print(json.dumps(result))
        conn.close()
        
    except Exception as e:
        throwErr(str(e) + "\nIncorrect login information.")
        return

#parsed_json = json.loads('{"firstname":"Cole", "lastname":"Sil", "phone":"1234567890", "email":"cole@gmail.com", "userid":2}')
parsed_json = getjson()
login(parsed_json)
