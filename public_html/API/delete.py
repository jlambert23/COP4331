#!/usr/bin/python3
# coding: utf-8

import util
print("Content-Type: application/json\n\n")

def delete(jsonPayload):
    import pymysql

    try:
        firstname = jsonPayload['firstname']
        lastname = jsonPayload['lastname']
        phone = jsonPayload['phone']
        email = jsonPayload['email']
        userid = jsonPayload['userid']
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
        # Remove contact from database.
        sql = "DELETE FROM contact WHERE firstname='%s' AND lastname='%s' AND phone='%s' AND email='%s' AND userid=%d;" % (firstname, lastname, phone, email, userid)
        cursor.execute(sql)        
        conn.commit()
        
        # Retrieve updated contact list.
        sql2 = "SELECT * FROM `contact` WHERE userid='%d';" % userid
        cursor.execute(sql2)        
        columns = cursor.description
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
		
        result = [userid] + result
        util.sendjson(result)
        conn.close()
        
    except:
        util.throwErr("Unable to delete contact.")
        return
        
try:
    #import json
    #parsed_json = json.loads('{"firstname":"Cole", "lastname":"Sil", "phone":"1234567890", "email":"cole@gmail.com", "userid":2}')
    parsed_json = util.getjson()
    delete(parsed_json)
except:
    util.throwErr("Failed to parse json.")
