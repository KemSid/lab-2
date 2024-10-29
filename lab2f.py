#!/usr/bin/env python3
# Author: Sidney Mills
# Author ID: KemSid
# Date Created: 2024/10/22

import sys

if len(sys.argv) < 2:
    print("Usage: ./lab2f.py <count>")
    sys.exit(1)

timer = int(sys.argv[1])

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
