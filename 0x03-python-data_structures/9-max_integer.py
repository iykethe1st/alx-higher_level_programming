#!/usr/bin/python3
def max_integer(my_list=[]):
    maxx = 0
    for num in my_list:
        if num > maxx:
            maxx = num
    return maxx
