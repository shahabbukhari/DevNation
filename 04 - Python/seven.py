import random

# times = input("How Many Times to like to roll a dice: ")
times = 5;
luckyTimes = 0

for i in range(int(times)):
    no1 = random.randint(1,6)
    no2 = random.randint(1,6)
    if (no1 + no2) == 7:
        luckyTimes = luckyTimes + 1
    print("no 1 is: ", no1)
    print("no 1 is: ", no2)

print("You Rolled Lucky 7: ", luckyTimes, " Times")