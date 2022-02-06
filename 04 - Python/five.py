# The Collatz Conjecture states that if you pick a number, and repeat a certain procedure, you will eventually arrive at the number 1 for any given natural number input.

# The procedure is as follows:
# If the number is odd, multiply it by 3 and add 1  (3n+1)
# If the number is even, divide it by 2 (n/2)

# Please write code that can take a positive integer input, check this conjecture, and print the “Collatz chain” as well as the total length of the chain. Refer to the below screenshot for further details:

num = int(input("Enter a random number: "))

# num = 385448.76213

chain = []
length = 0
while num > 1:
    if (num % 2) == 0:
        num = int(num/2)
        chain.append(num)
        # print("Even: ", num)
    else:
        num = int(3*num + 1)
        chain.append(num)
        # print("Odd: ", num)
    length = length + 1

print("The chain: ", chain)
print("No of Steps it took: ", length)
