
def countingValleys(steps, path):
    # Write your code here
    rider_position = 0
    count = 0 
    isValidValley = False
    for i in path:
        if isValidValley:
            if rider_position == 0:
                count +=1
        if i == 'U':
            rider_position += 1
            if rider_position > 0:
                isValidValley = False
        elif i == 'D':
            if rider_position <= 0:
                isValidValley = True
            rider_position -= 1
        print("i:",i,'rider position:',rider_position,'count:', count, 'and is it valid valley:', isValidValley)
    if rider_position == 0 and isValidValley:
        count += 1
    return count

# print(countingValleys(8,'UDUDDUUUDUDUDUUDUUDDDDDUDUDDDDUUDDUDDUUUUDUUDUDDDDUDUDUUUDDDUUUDUDDUUDDDUUDDUDDDUDUUDUUDUUDUDDDUUUUU'))
print(countingValleys(8, 'DDUUDDUDUUUD'))
