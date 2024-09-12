#!/usr/bin/python3
import sys
len = len(sys.argv)
result = 0
for i in range(len):
    if i > 0:
        result += int(sys.argv[i])
print(result)
