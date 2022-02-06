def pageCount(n, p):
    # Write your code here
    positions = [0, 0]
    start_pages = [0, 1]
    for i in range(n):
        if p in start_pages:
            positions[0] = i
            break
        else:
            start_pages[0] += 2
            start_pages[1] += 2

    end_pages = [n-1, n]
    for i in range(n):
        if p in end_pages:
            positions[1] = i
            break
        else:
            end_pages[0] -= 2
            end_pages[1] -= 2

    # return min(positions)
    print(positions)


print(pageCount(6, 5))
print(pageCount(5, 4))
