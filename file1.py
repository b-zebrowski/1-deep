#!/usr/bin/python
import requests
# This is a single line comment, you should not see the link to https://github.com/accountnotexist/some-repo

'''
Now lets check a multi-line comment, you should not see a link to https://github.com/accountnotexist/some-repo
'''
"""
Another multi-line comment, you should not see a link to https://github.com/accountnotexist/some-repo
"""
bla = requests.get('https://github.com/accountdoesnotexist/some-repo') # this line you should see pointing to a non-existent user
bla2 = requests.get('https://github.com/accountdoesnotexist/some-repo@123456') # same user, but calling a specific tag
