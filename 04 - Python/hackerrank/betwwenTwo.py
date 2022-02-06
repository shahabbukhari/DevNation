import collections


def getTotalX(a, b):
    # Write your code here
    arr_1 = a
    arr_2 = b
    arr_2_max = max(arr_2)
    factors_list = []
    matching_factors = []

    for j in range(1, arr_2_max+1):
        isAllAgree = True
        for k in arr_2:
            if k % j != 0:
                isAllAgree = False
        if isAllAgree:
            factors_list.append(j)

    for i in factors_list:
        isValidFactor = True
        for j in arr_1:
            if i % j != 0:
                isValidFactor = False
        if isValidFactor:
            matching_factors.append(i)

    return len(matching_factors)


print(getTotalX([1], [100]))

# for i in arr_2:
# print("the factor ", i, "are")
# for j in range(1, i+1):
#     if i % j == 0:
#         factors_list.append(j)

# counts = collections.Counter(factors_list)
# list_with_factors_duplication = []
# for i in counts:
#     if counts[i] >= len(arr_2):
#         # print("at", i, "we have ", counts[i], "elements")
#         list_with_factors_duplication.append(i)
