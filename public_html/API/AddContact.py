
#!/usr/bin/python
# coding: utf-8

def addcontact(name, phone, email):
    import pymysql

    try:
        conn = pymysql.connect(
            host='localhost',
            db='COP4331',
            user='db-sys',
            password=''
        )
        cursor = conn.cursor()

        sqlAdd = "INSERT INTO contacts (name,phone,email) VALUES ('name','phone','email');"
        cursor.execute(sqlAdd)

        message = name + " has been added to your contacts."
        conn.close()

    except Exception as e:
        message = "Unable to add contact " + name + "\n\n" + str(e)

    return message
#

import sys
import json
# parsed_json = json.loads(json_string)
# parsed_json = json.load(sys.stdin)

json_string = '{"name": "Guido", "phone":"123-456-7890", "email": "computers@nerds.org"}'
parsed_json = json.loads(json_string)

name = parsed_json['name']
phone = parsed_json['phone']
email = parsed_json['email']

message = addcontact(name, phone, email)

print( message )

#header = "Content-type: application/json\n\n"
#print(header + json.dumps(parsed_json))