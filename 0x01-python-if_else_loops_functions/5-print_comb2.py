#!/usr/bin/python3
for num in range(100):
    if num == 99:
        print("{}".format(num))
    elif num < 99:
        if num < 10:
            num = "0" + str(num)
        print("{}".format(num), end=", ")    
