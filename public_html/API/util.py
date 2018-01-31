import json

def throwErr(message):
    print(json.dumps({'error': "" + message + ""}))
    
def getjson():
    import sys
    return json.load(sys.stdin)
    
def sendjson(message):
    print(json.dumps(message))
    
