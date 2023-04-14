import urllib.request
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    x_request_id = response.getheader("X-Request-Id")
    print("X-Request-Id: {}".format(x_request_id))

