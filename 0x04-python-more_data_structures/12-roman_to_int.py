#!/usr/bin/python3
def get_value(x):
    if (x == 'I'):
        return 1
    if (x == 'V'):
        return 5
    if (x == 'X'):
        return 10
    if (x == 'L'):
        return 50
    if (x == 'C'):
        return 100
    if (x == 'D'):
        return 500
    if (x == 'M'):
        return 1000
    return -1


def roman_to_int(roman_string):
    sum = 0
    i = 0

    if not (isinstance(roman_string, str)) or roman_string == None:
        return 0
 
    while (i < len(roman_string)):
        num1 = get_value(roman_string[i])
        
        if (i + 1 < len(roman_string)):
            num2 = get_value(roman_string[i + 1])
        
            if (num1 >= num2):
                sum += num1
                i += 1
        
            else:
                sum += num2 - num1
                i += 2
        else:
            sum += num1
            i += 1
    return sum
