arr = [1, 4, 4, 4, 5, 3]

occurrences = {}
for i in arr:
    if i in occurrences:
        occurrences[i] += 1
    else:
        occurrences[i] = 1

maxValue = {"birds": [], "occur": 0}
for i in occurrences:
    if occurrences[i] > maxValue["occur"]:
        if i in maxValue["birds"]:
            # maxValue["occur"] = occurrences[i]
            pass
        else:
            maxValue["birds"] = [i]
            maxValue["occur"] = occurrences[i]

    elif occurrences[i] == maxValue["occur"]:
        if i in maxValue["birds"]:
            # maxValue["occur"] = occurrences[i]
            pass
        else:
            maxValue["birds"].append(i)
            maxValue["occur"] = occurrences[i]
print(occurrences)
print(maxValue)
print(min(maxValue['birds']))


# count = {}
# arr.sort()
# max_value = 0
# # print(arr)
# for i in arr:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1
# # print(count)
# max_key = max(count, key=count.get)

# print(max_key)
