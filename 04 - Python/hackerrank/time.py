
s = "07:05:45PM"
# s = "12:01:00AM"
sList = s.split(":")
period = sList[-1][-2] + sList[-1][-1]
hour = int(sList[0])
minutes = int(sList[1])
sec = int(sList[2][0] + sList[2][1])

if period == "AM" and hour >= 12 and hour < 24:
    hour = 00
elif period == "PM" and hour != 12:
    hour += 12

if minutes < 10:
    minutes = "0" + str(minutes)
if sec < 10:
    sec = "0" + str(sec)
if hour < 10:
    hour = "0" + str(hour)


result = str(hour) + ":" + str(minutes) + ":" + str(sec)
print(result)
