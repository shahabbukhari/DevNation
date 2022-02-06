# print the following patterns using loop :
# a.
# *
# **
# ***
# ****
for j in range(1, 5, 1):
    print(j*"*")

# b.
#    *
#  ***
# *****
#  ***
#    *


def pr(str, end, stp):
    for i in range(str, end, stp):
        if end > 0:
            print((end-(i+1))*" "+i*"*")
        else:
            print((str-(i+1))*" "+i*"*")

def startPara(ss):
    pr(1, ss, 2)
    pr(ss, 0, -2)

startPara(5)

# c.
# 1010101
#  10101
#   101
#    1
def pyramid(size):
    space = 0
    for c in range(size, -1, -1):
        print(space*" "+(c*"10")+"1")
        space = space + 1


# size = input("Size of Binary pyramid")
size = 10
pyramid(int(size))


# Multi Paramid
# def pyramid(str, end, stp):
#     space = 0
#     for c in range(str, end, stp):
#         if str > 0:
#             print(space*" "+(c*"10")+"1")
#             space = space + 1
#         else:
#             print((end-(c+1))*" "+(c*"10")+"1")


# # size = input("Size of Binary pyramid")
# def startPyramid(str):
#     pyramid(str, -1, -1)
#     pyramid(0, str+1, 1)

