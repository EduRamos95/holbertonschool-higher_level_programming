#!/usr/bin/python3
def best_score(a_dictionary):
    result = 0
    winner = None
    if a_dictionary is not None or len(a_dictionary) == 0:
        for key in a_dictionary:
            if a_dictionary[key] > result:
                result = a_dictionary[key]
                winner = key
        return winner
    return None
