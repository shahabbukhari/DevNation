# flagL = input("How long is your flag? ")
# flagW = input("How wide is your flag? ")
# flagPL = input("How long is your flagPole? ")
# flagPW = input("How wide is your flagPole? ")
flagL = 5
flagW = 10
flagPL = 6
flagPW = 2

def flag(FL,FW,FPL,FPW):
    for i in range(FL):
        print(FW*"*")
    for j in range(flagPL):
        print(FPW*"*")

flag(flagL,flagW,flagPL,flagPW)