import urllib.parse
import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode()
req = urllib.request.Request(url, data)

with urllib.request.urlopen(req) as response:
    body = response.read()
    print(body.decode('utf-8'))

