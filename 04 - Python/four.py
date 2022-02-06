my_list = [1, 22, 32, 12, 55, 88, 76, 54, 2, 1, 22, 33, 44, 5, 6, 6, 7, 5, 0]
# Average = sum / no. of items
sumOf = 0
length = 0

for a in my_list:
    sumOf = sumOf + a
    length = length + 1

print(sumOf/length)
