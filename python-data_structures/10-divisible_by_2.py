#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    new_list = []
    for element in my_list:
        new_list.append(False if element % 2 else True)
    return new_list
