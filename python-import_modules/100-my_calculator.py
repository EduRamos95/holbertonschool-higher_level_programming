#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)
    a, operator, b = (int(argv[1]), argv[2], int(argv[3]))
    func_to_operator = {"+": add, "-": sub, "*": mul, "/": div}
    if operator not in func_to_operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {:s} {:d} = {:d}"
          .format(a, operator, b, func_to_operator[operator](a, b)))
