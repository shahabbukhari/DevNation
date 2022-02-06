# # a = [1]
# b = [100]


a = [3, 4]
b = [24, 48]
maxA = max(a)  # 4
minB = min(b)  # 24
multiples = []


for i in range(maxA, minB + 1, maxA):  # 24/6 = 4
    multiples.append(i)

print("Multiples:", multiples)
count = 0
for i in multiples:
    if i < minB:
        if minB % i == 0:
            count += 1
    else:
        if i % minB == 0:
            count += 1

print(count)
