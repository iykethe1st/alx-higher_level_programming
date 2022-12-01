#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total_arg = len(sys.argv)
    total = 0
    for i in range(1, total_arg):
        total += int(sys.argv[i])
    print("{}".format(total))
