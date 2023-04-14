#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}

    r = requests.post(url, data=data)
    try:
        response = r.json()
        if response:
            print("[{}] {}".format(response['id'], response['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")

