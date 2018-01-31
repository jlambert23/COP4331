#!/usr/bin/python3
# coding: utf-8

import util
print("Content-Type: application/json\n\n")
    
def add(jsonPayload):
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
        # Add contact to database.
        sql = "INSERT INTO contact (firstname,lastname,phone,email,userid) VALUES ('%s','%s','%s','%s',%d);" % (firstname, lastname, phone, email, userid)
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
        util.throwErr("Unable to add contact.")
        return
   
try:
    #import json
    #parsed_json = json.loads('{"firstname":"Cole", "lastname":"Sil", "phone":"1234567890", "email":"cole@gmail.com", "userid":2}')
    parsed_json = util.getjson()
    add(parsed_json)
except:
    util.throwErr("Failed to parse json.")
    