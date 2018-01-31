#!/usr/bin/python
# coding: utf-8

def removecontact(json):
    try:
        import pymysql

        id = json['id']
        name = json['name']
        userid = json['userID']

        # Import connection settings.
        from dbsettings import connection_properties
        conn = pymysql.connect( **connection_properties )
        cursor = conn.cursor()

        from SearchContact import searchcontact
        if not searchcontact(json):
            raise Exception(name + " is not found in your contacts.")

        sql = "DELETE FROM contact WHERE name='%s' AND userID=%d;" % (name, userid)
        cursor.execute(sql)
        conn.commit()

        message = name + " has been removed from your contacts."

        # Print data from table.
        #cursor.execute("SELECT * FROM contact;")
        #print(cursor.fetchall())

        conn.close()

    except Exception as e:
        message = "Unable to remove contact " + name + ".\n" + str(e)
        sendjson('{"error":"' + message + '"}')

    return message

def getjson():
    import sys
    return json.load(sys.stdin)

def sendjson(message):
    header = "Content-type: application/json\n\n"
    print(header + json.dumps(message))

# ======================= #
# -- STILL IN PROGRESS -- #
# ======================= #
import json
#parsed_json = getjson()

# -- Testing --
json_string = '{"id":1, "name": "Johnny", "phone":"123-456-7890", "email":"computers@nerds.org", "userID":1}'
parsed_json = json.loads(json_string)

message = removecontact(parsed_json)
print(message)