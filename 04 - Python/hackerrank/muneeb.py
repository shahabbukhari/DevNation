s = [2, 2, 1, 3, 2]
m = 2
d = 4


def birthday(s, d, m):
    count = 0
    if len(s) == 1 and s[0] == d:
        return 1
    count = 0
    for i in range(len(s)-m+1):
        sum = 0
        index = i
        for j in range(m):
            sum = sum + s[index]
            index += 1
        if sum == d:
            count += 1
    return count


print(birthday(s, d, m))
