#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return None
    num_index = range(len(my_list)-1, -1, -1)
    for index in num_index:
        print("{:d}".format(my_list[index]))