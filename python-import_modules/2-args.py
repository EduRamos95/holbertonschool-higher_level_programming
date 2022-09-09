#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
#   user_input = argv[1:]
    num_arg = len(argv) - 1
    print("{:d} {:s}{:s}".
          format(size,
                 "arguments" if (size) is not 1 else "argument",
                 "." if (size) is 0 else ":"))
    for index in range(1, (num_arg + 1)):
        print("{}: {}".format(i, sys.argv[i]))
