#!/bin/bash
# Script that displays the Content-Length from a HTTP request
curl -s "$1" | wc -c
