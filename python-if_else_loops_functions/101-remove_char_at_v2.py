#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    if n >= 0:
        str2 = str2[:n] + str2[n+1:]
    return str2
