#!/usr/bin/env python3
# coding: utf-8

json_string = '{"username": "Guido", "password":"Rossum"}'

import sys
import json
# parsed_json = json.loads(json_string)
parsed_json = json.load(sys.stdin)

first_name = parsed_json['username']
last_name = parsed_json['password']

# <-- MySQL code will go here! -->

header = "Content-type: application/json\n\n"
print(header + json.dumps(parsed_json))
