#!/usr/bin/env python3
# coding: utf-8

json_string = '{"username": "cop4331", "password":"pass"}'

import sys
import json
import pymysql
#parsed_json = json.loads(json_string)
parsed_json = json.load(sys.stdin)

first_name = parsed_json['username']
password = parsed_json['password']


#<-- MySQL code will go here! -->
# Gabes SQL Edit##################
#    conn = pymysql.connect(
#    host='localhost',
#    db='jayTest',
#    user='db-sys',
#    password=''
#)

conn = pymysql.connect(host= 'localhost', user= 'db-sys', password = '', db= 'jayTest')
cursor = conn.cursor()
#sql = "SELECT `id` FROM users WHERE user="+first_name+" AND passwd="+password
#cursor.execute("SELECT id FROM users WHERE user="+first_name+" AND passwd="+passwd)
#result = cursor.fetchone()
#conn.close()
#json_output = {}
#json_output['id'] = result #'{"id": "'+result+'"}'

#asdfasdfasdfasdfasdf#S
sql = "SELECT id FROM users WHERE user='"+first_name+"' AND passwd='"+password+"';"
cursor.execute(sql)
#cursor.execute("SELECT id FROM users WHERE common_schema.extract_json_value(parsed_json,'password')")
result = cursor.fetchone()
#conn.close()
json_output = {}
json_output['id'] = result[0]
#adfasdfasdfasdfasdfa#

##################################

header = "Content-type: application/json\n\n"
print(header + json.dumps(json_output))
conn.close()
