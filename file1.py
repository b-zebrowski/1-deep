#!/usr/bin/python
import requests
# This is a single line comment, you should not see the link to https://github.com/accountnotexist/some-repo

'''
Now lets check a multi-line comment, you should not see a link to https://github.com/accountnotexist/some-repo
'''
"""
Another multi-line comment, you should not see a link to https://github.com/accountnotexist/some-repo
"""

def fetch_url(url):
    try:
        # Perform the HTTP GET request
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            print(f"Response from {url}:\n")
            print(response.text)  # Print the response body
        else:
            print(f"Failed to fetch the URL. HTTP Status: {response.status_code} - {response.reason}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

# Specify the URL
url = "https://github.com/accountdoesnotexist/some-repo" # this line you should see pointing to a non-existent user

print(f"Fetching URL: {url}\n")
fetch_url(url)

url = "https://github.com/accountdoesnotexist/some-repo@123456" # same user, but calling a specific tag

print(f"Fetching URL: {url}\n")
fetch_url(url)
