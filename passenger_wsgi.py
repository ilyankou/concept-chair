import os
import sys
import json
import urllib
import random
import cgitb
from cgi import parse_qs, escape

sys.path.insert(0, os.path.dirname(__file__))

def application(environ, start_response):

    d = parse_qs(environ['QUERY_STRING'])
    n = d.get('n', [''])[0]
    res = '{"n": '

    try:
        x = int(n)
        f = open('n.json','w')
        f.write('{"n": ' + str(x) + '}')
        f.close()
        res += n + "}"
    except:
        data = json.load(open('n.json'))
        res += str(data['n']) + "}"

    start_response('200 OK', [('Content-Type', 'text/plain'), ('Access-Control-Allow-Origin', '*')])
    return [res]
