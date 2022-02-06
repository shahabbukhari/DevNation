ame = "8hypotheticall024y6wxz"
final = ""
resChar = ""
resNum = ""
tempnum = ""
tempchar = ""
totalNum = "0123456789"
totalChar = "abcdefghijklmnopqrstuvwzyz"

for i in ame:
    if str.isdigit(i):
        tempnum += i
    else:
        tempchar += i
# tempchar = "".join(OrderedDict.fromkeys(tempchar))

for i in tempchar:
    for j in totalChar:
        if i == j:
            totalChar = totalChar.replace(i, "")
            # print("in if i and j", i, j)

for i in tempnum:
    for j in totalNum:
        if i == j:
            totalNum = totalNum.replace(i, "")
result = totalNum+totalChar

print(result)
