#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    n_d = {k: v for k, v in a_dictionary.items() if k != key}
    a_dictionary.clear()
    a_dictionary.update(n_d)
    return a_dictionary

