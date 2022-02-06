from itertools import count
import math


def sockMerchant(n, ar):
    # Write your code here
    occur = {}
    for i in ar:
        if i in occur:
            occur[i] += 1
        else:
            occur[i] = 1
    count = 0
    print(occur)
    for i in occur:
        pair = math.floor(occur[i]/2)
        count += pair

    print(count)


arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
sockMerchant(0, arr)
