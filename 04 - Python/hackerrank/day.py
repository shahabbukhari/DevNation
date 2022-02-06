def dayOfProgrammer(year):
    # Write your code here

    if year > 1918 and year <= 2700:
        # leap year is
        #
        #
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return "12.09."+str(year)
        else:
            return "13.09."+str(year)

    if year >= 1700 and year < 1918:
        # leap year then
        if year % 4 == 0:
            return "12.09."+str(year)
        else:
            return "13.09."+str(year)
    if year == 1918:
        return "26.09."+str(year)
