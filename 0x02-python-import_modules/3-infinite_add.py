#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    arg = sys.argv
    length = len(arg) - 1
    sum = 0

    for i in range(1, length + 1):
        sum = sum + int(arg[i])
print("{}".format(sum))
