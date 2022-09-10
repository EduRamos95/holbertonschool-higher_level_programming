#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_arg = len(argv) - 1
    print("{:d} {:s}{:s}".
          format(num_arg,
                 "arguments" if (num_arg) != 1 else "argument",
                 "." if (num_arg) == 0 else ":"))
    for index in range(1, (num_arg + 1)):
        print("{}: {}".format(index, argv[index]))
