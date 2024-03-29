#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response
If HTTP status code >= 400, print: Error code + value of the HTTP status code
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
