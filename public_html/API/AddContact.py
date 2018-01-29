#!/usr/bin/python
# coding: utf-8

def addcontact(json):
    import pymysql

    name = json['name']
    phone = json['phone']
    email = json['email']
    userID = json['userID']

    try:
        conn = pymysql.connect(
            host='localhost',
            db='example',
            user='db-sys'
        )
        cursor = conn.cursor()


        sqlAdd = "INSERT INTO contact (name,phone,email,userID) VALUES ('%s','%s','%s',%d);" % (name, phone, email, userID)
        cursor.execute(sqlAdd)

        message = name + " has been added to your contacts."

        sqlRetrieve = "SELECT * FROM contact;"
        cursor.execute(sqlRetrieve)

        print(cursor.fetchall())

        conn.close()

    except Exception as e:
        message = "Unable to add contact " + name + "\n\n" + str(e)

    return message

def getjson():
    import sys
    return json.load(sys.stdin)




import sys
import json
# parsed_json = json.loads(json_string)
# parsed_json = json.load(sys.stdin)

json_string = '{"name": "Guido", "phone":"123-456-7890", "email":"computers@nerds.org", "userID":1}'

# parsed_json = json.loads(json_string)
parsed_json = getjson()

message = addcontact(parsed_json)
print( message )

#header = "Content-type: application/json\n\n"
#print(header + json.dumps(parsed_json))
