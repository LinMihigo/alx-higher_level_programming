#!/bin/bash
# Sends a JSON post request to a url. Displays body of response
curl -s -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
