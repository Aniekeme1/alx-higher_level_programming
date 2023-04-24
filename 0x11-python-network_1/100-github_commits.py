#!/usr/bin/python3

import requests
import sys

# Get repository name and owner name from command line arguments
repo_name = sys.argv[1]
owner_name = sys.argv[2]

# Send GET request to GitHub API to get 10 most recent commits
response = requests.get(f"https://api.github.com/repos/{owner_name}/{repo_name}/commits")

# Check if response status code is successful
if response.status_code == 200:
    # Loop through each commit in response and print commit hash and author name
    for commit in response.json()[:10]:
        print(f"{commit['sha']}: {commit['commit']['author']['name']}")
else:
    # Print error message if status code is not successful
    print(f"Error retrieving commits from {owner_name}/{repo_name}. Status code: {response.status_code}")

