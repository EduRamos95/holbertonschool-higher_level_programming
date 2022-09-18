#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as error:
        stderr.write("Exception: {}\n".format(error))
#       print("Exception: {}".format(error), file=sys.stderr)
        return (False)
