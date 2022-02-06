def divisibleSumPairs(n, k, ar):
    # Write your code here
    count = 0
    for i in ar:
        for j in ar:
            if (i < j) and (i+j) % k == 0:
                count += 1
    return count


ar = [1, 2, 3, 4, 5, 6]
k = 5
print(divisibleSumPairs(0, k, ar))
