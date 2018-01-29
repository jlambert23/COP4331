#!/usr/bin/env python3
# coding: utf-8

json_string = '{"username": "Guido", "password":"Rossum"}'

import sys
import json
import pymysql
# parsed_json = json.loads(json_string)
parsed_json = json.load(sys.stdin)

first_name = parsed_json['username']
password = parsed_json['password']

# <-- MySQL code will go here! -->
# Gabes SQL Edit##################
#    conn = pymysql.connect(
#    host='localhost',
#    db='jayTest',
#    user='db-sys',
#    password=''
#)
#cursor = conn.cursor()

#sql = "SELECT `id` FROM users WHERE user="+first_name+" AND passwd="+password
#cursor.execute("SELECT id FROM users WHERE user="+first_name+" AND passwd="+passwd)
#result = cursor.fetchone()
#conn.close()
#json_output = {}
#json_output['id'] = result #'{"id": "'+result+'"}'

##################################

header = "Content-type: application/json\n\n"
print(header + json.dumps(json_string))
conn.close()
