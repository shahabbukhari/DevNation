# from itertools import count


# m = 2
# [2,2] , [2,1] , [2,3] , [2,2]
# [2,1] , [2,3] , [2,2]
# [1,3] , [1,2]
#         pairs.append(s[j])
# [3,2]

# s = [1, 2, 3, 4, 5, 6, 7]

# pairs = []
# for i in range(len(s)):
#     for j in range(i+1, len(s)):
#         pairs.append(s[i])

# print(pairs)

# m = 2

# for i in range(len(pairs)):
#     if (pairs[i][0] + pairs[i][1]) == d:
#         valid_array.append([pairs[i][0], pairs[i][1]])

# s = [3, 5, 4, 1, 2, 5, 3, 4, 3, 2, 1, 1, 2, 4, 2, 3, 4, 5, 3, 1, 2, 5, 4, 5, 4, 1, 1,
#      5, 3, 1, 4, 5, 2, 3, 2, 5, 2, 5, 2, 2, 1, 5, 3, 2, 5, 1, 2, 4, 3, 1, 5, 1, 3, 3, 5]
# 2 , 2, 1
# 2 , 1 , 3
# 1, 3, 2

s = [1, 2, 3, 4, 5, 6, 7]
print(s[6:10])
m = 2
d = 3
valid_array = []
pairs = []
# for i in range(len(s)):
#     for j in range(i+1, len(s)):
#         if [s[i], s[j]] not in pairs:
#             pairs.append([s[i], s[j]])

# print(pairs)


for i in range(len(s)):
    if sum(s[i:i+m]) == d:
        valid_array.append(s[i:i+m])
# print(pairs)
print(len(valid_array))
print(valid_array)
