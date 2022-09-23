#!/usr/bin/python3
import sys

arg = sys.argv
length = len(arg) - 1

if length == 0:
    print("0 arguments")
elif length == 1:
    print("{} argument:".format(length))
    print("{}: {}".format(length, arg[length]))
elif length > 1:
    print("{} arguments:".format(length))
    for i in range(length):
        print("{}: {}".format(i + 1, arg[i + 1]))
