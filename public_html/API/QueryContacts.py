#!/usr/bin/env python3
# coding: utf-8

import json

def query(json):
    import pymysql

    try:
        userid = json['userID']
    except:
        throwErr("JSON incorrectly configured.\n%s" % json)
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
        sql = "SELECT * FROM `contact` WHERE userID='%d';" % userid
        cursor.execute(sql)
        
        columns = cursor.description 
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

        sendjson(result)
        conn.close()
    except:
        sendjson('{"error":"Unable to retrieve contacts."}')

def getjson():
    import sys
    return json.load(sys.stdin)

def sendjson(message):
    header = "Content-type: application/json\n\n"
    print(header + json.dumps(message))

def throwErr(message):
    sendjson('{"error":"%s"}' % message)

#parsed_json = getjson()
parsed_json = json.loads('{"userID":"2"}')
query(parsed_json)
