from collections import Counter


def pickingNumbers(a):
    # Write your code here
    myyArr = Counter(a)
    maxNum = 0
    for i in range(1, 100):
        maxNum = max(maxNum, myyArr[i]+myyArr[i+1])
        # print(i, ":", myyArr[i], i+1, ":", myyArr[i+1], "MAXNUM: ", maxNum)
    return maxNum


pickingNumbers([1, 2, 2, 3, 1, 2])
