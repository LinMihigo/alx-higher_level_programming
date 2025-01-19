#!/bin/bash
# Sends a request to a URL and display status code of response
curl -o /dev/null -s -w "%{http_code}" "$1"
