def breakingRecords(scores):
    # Write your code here
    minimum = None
    maximum = None
    minCount = 0
    maxCount = 0
    score = 8
    for score in scores:
        if minimum == None and maximum == None:
            maximum = score
            minimum = score
        elif score > maximum:
            maxCount += 1
            maximum = score
        elif score < minimum:
            minCount += 1
            minimum = score

    print(maxCount, minCount)


arr_1 = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
breakingRecords(arr_1)
