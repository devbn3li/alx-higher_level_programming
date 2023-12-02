#!/usr/bin/python3
"""Display the X-Request-Id header variable of a request to a given URL
"""


if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
