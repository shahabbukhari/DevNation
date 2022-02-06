import math


def gradingStudents(grades):
    # Write your code here
    roundedList = []

    for i in grades:
        multiple = 5 * math.ceil(i/5)
        roundedGrade = 0
        if i < 40 and i+2 < 40:
            roundedGrade = i
        elif (multiple - i) < 3:
            roundedGrade = i + (multiple - i)
        else:
            roundedGrade = i
        roundedList.append(roundedGrade)

    return roundedList


print(gradingStudents([73, 67, 38, 33]))
