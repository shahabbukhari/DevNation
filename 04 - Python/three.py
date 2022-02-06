# Question 3: Calculate the average

#  Write a program that takes integer inputs from the user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.

# Average  => sum/length
# Product => mul

sumOf = 0;
size = 1;
product = 1;
num = 0;
run = True;


while run:
    num = input("Enter integer: ");
    ask = input("want to exit(enter q): ");
    
    num = int(num);
    sumOf = sumOf + num;
    size = size + 1;
    product = product * num;
    
    if ask == "q":
        run = False;
    
print("the average is:",sumOf/size);
print("the product is:",product);