#!/usr/bin/python
# coding: utf-8

def addcontact(json):
    import pymysql

    try:
        name = json['name']
        phone = json['phone']
        email = json['email']
        user_id = json['userID']

        # Import connection settings.
        from dbsettings import connection_properties
        conn = pymysql.connect( **connection_properties )
        cursor = conn.cursor()

        # Check if contact already exists.
        #sql = "SELECT * FROM contact WHERE name='%s' AND phone='%s' AND email='%s' AND userID=%d" % (name, phone, email, user_id)
        #cursor.execute(sql)

        from SearchContact import searchcontact
        if searchcontact(json):
            raise Exception(name + " is already found in your contacts.")


        # Insert data to contact table.
        sql_add = "INSERT INTO contact (name,phone,email,userID) VALUES ('%s','%s','%s',%d);" % (name,phone,email,user_id)
        cursor.execute(sql_add)
        conn.commit()

        message = name + " has been added to your contacts."

        # Print data from table.
        #cursor.execute("SELECT * FROM contact;")
        #print(cursor.fetchall())

        conn.close()

    except Exception as e:
        message = "Unable to add contact " + name + ".\n" + str(e)
        sendjson('{"error":"' + message + '"}')

    return message

def getjson():
    import sys
    return json.load(sys.stdin)

def sendjson(message):
    header = "Content-type: application/json\n\n"
    print(header + json.dumps(message))


import json
#parsed_json = getjson()

# -- Testing --
json_string = '{"name": "Johnny", "phone":"123-456-7890", "email":"computers@nerds.org", "userID":1}'
parsed_json = json.loads(json_string)

message = addcontact(parsed_json)
print(message)

