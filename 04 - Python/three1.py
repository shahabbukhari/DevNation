str = "ABCd"
# str = input("Enter a String ")

evenSum = 0
oddSum = 0
sum = 0

def evenS(ascii):
    evenSum += ascii


def oddS(ascii):
    oddSum += ascii

def sumOf():
    sum = evenSum + oddSum 

for i in range(1,len(str)+1):
    ascii = ord(str[i-1]) 
    if (i % 2) == 0:
        evenS(ascii)
    else:
        oddS(ascii)

print("Total ASCII Sum:", sum)
print("ASCII Sum of odd-numbered characters:", oddSum)
print("ASCII Sum of even-numbered characters:", evenSum)
