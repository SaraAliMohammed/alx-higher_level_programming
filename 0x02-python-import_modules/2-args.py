#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args_count = len(argv)
    if args_count == 0:
        print("0 argument.")
    elif args_count == 1:
        print("1 argument.")
    else:
        print("{} arguments:".format(args_count))
    for i in range(args_count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
