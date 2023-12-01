#!/bin/bash
# Script to GET request and SHOW the response status code.
curl -s -o /dev/null -w "%{http_code}" "$1"
