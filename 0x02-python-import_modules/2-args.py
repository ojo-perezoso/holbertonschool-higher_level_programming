#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = (len(sys.argv))

    if (argc == 1):
        print("0 arguments.")
        exit()
    if (argc == 2):
        print("1 argument:")
    else:
        print("{:d} arguments:".format(argc - 1))

    for i in range(1, argc):
        print("{:d}: {}".format(i, sys.argv[i]))
