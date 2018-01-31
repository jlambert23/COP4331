#!/usr/bin/python3
#print("Content-Type: text/html\n\n")

import json

def getjson():
    import sys
    return json.load(sys.stdin)

def sendjson(message):
    print(json.dumps(message))

def throwErr(message):
    sendjson('{"error":"%s"}' % message)
	
def query(json):
    import pymysql

    try:
        userid = json['userid']
    except:
        throwErr("JSON incorrectly configured.\n" + json)
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
        sql = "SELECT * FROM `contact` WHERE userID='" + userid + "';"
        cursor.execute(sql)
        
        columns = cursor.description 
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

        conn.close()
        return result
    except:
        throwErr("Unable to retrieve contacts.")


#parsed_json = getjson()
#query(parsed_json)