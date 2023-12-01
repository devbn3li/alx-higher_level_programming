#!/bin/bash
# Script to do a JSON POST request with a provided JSON file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
