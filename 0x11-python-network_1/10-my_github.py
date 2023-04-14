import requests
import sys

if len(sys.argv) != 3:
    print("Usage: {} Aniekeme1 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".format(sys.argv[0]))
    sys.exit(1)

username = sys.argv[1]
token = sys.argv[2]

url = "https://api.github.com/Aniekeme1"

response = requests.get(url, auth=(username, token))

if response.status_code == 200:
    data = response.json()
    print("Your GitHub ID is: {}".format(data['id']))
else:
    print("Failed to fetch user information. Error code: {}".format(response.status_code))

