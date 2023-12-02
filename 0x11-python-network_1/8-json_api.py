#!/usr/bin/python3
"""A script tha:
takes in a letter
sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""

if __name__ == "__main__":
    import requests
    import sys
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"

    res = requests.post(url, data={"q": q})
    try:
        resp = res.json()
        if resp:
            print(f"[{resp.get('id')}] {resp.get('name')}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
