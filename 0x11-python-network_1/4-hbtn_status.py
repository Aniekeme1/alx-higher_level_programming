#!/usr/bin/env python3
import requests

url = "https://alx-intranet.hbtn.io/status"
response = requests.get(url)

print("Body response:")
print("\t- type:", type(response.text))
print("\t- content:", response.text)

