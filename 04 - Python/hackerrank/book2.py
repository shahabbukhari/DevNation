def pageCount(n, p):
    # Write your code here
    page_turns_front = 0
    # page_side=0
    page_side = 0
    # checking from front
    # loop till the n
    for i in range(n):
        # check if pages are two
        if page_side == 2:
            page_turns_front += 1
            page_side = 0
        # page_turns_front+=1
            # page_side=0
        # check if i==p:
        if i == p:
            #   break
            break
        # else:
        else:
            # page_side+=1
            page_side += 1
    # checking from back
    page_side = 0
    page_turns_back = 0
    for i in range(n, 0, -1):
        # check if pages are two
        if page_side == 2:
            page_turns_back += 1
            page_side = 0
        # page_turns_front+=1
            # page_side=0
        # check if i==p:
        if i == p:
            #   break
            break
        # else:
        else:
            # page_side+=1
            page_side += 1
        # print("i : ", i)
    return(min(page_turns_front, page_turns_back))


print(pageCount(6, 5))
