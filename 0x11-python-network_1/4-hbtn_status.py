#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""


import requests
response = requests.get('https://alx-intranet.hbtn.io/status')

content = response.text
print("Body response:")
print(f"\t- type: {type(content)}")
print(f"\t- content: {content}")
