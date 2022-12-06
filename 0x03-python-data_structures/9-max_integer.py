#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) is 0:
        return None
    maxx = my_list[0]
    for i in range(len(my_list)):
        if maxx < my_list[i]:
            maxx = my_list[i]
    return maxx
