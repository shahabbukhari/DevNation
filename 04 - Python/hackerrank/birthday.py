from threading import local


def birthdayCakeCandles(candles):
    # Write your code here
    candles.sort()
    times = 1
    position = -1

    def candle():
        nonlocal position
        nonlocal times
        if candles[position] == candles[position-1]:
            position -= 1
            times += 1
            candle()
        else:
            return

    candle()
    return times


arr = [9814373, 9422780, 3416228, 5649974, 2099099, 9999933, 7521656, 4379449, 3733801, 7928327, 7905107, 507867, 3195301, 5011643, 8797248, 4475721, 9999933, 2067372, 8900066, 8459769, 8490283, 9077365, 273921, 7700039, 7604286, 7418867, 5050895, 3388105, 6604693, 9195343, 3534755, 6285338, 7066783, 1774217, 9999933, 3353199, 3302363, 9999933, 8117591, 7673926, 3505424, 4859145, 7579450, 2723660, 592978, 7200960, 372074, 7141133, 8326964, 4214797, 4124202, 9999933, 9865514, 9973704, 9999933, 9999933, 4245977, 3452581, 261224, 9026103, 2562027, 6954971, 1551928, 4827337, 2113764, 5908368, 5354983, 9649194, 1275270, 6320211, 4649870, 4486703, 4109747, 8565181, 8493776, 3176989, 116849, 9705362, 8480843, 9168001, 411518, 9999933, 4896461, 8831278, 9999933, 387011, 7398427, 8891132, 6670585, 6781699, 3133542, 8412831, 7055378, 6213898, 9699223, 6256193, 4886025, 2228670, 7111195,
       9999933, 5723719, 5757572, 6264105, 4605594, 6751993, 4054686, 9999933, 9234053, 3397984, 9012354, 6837211, 6601805, 1659210, 4806900, 1784381, 9999933, 9455274, 2092547, 3319285, 7093509, 5520139, 5859111, 9428710, 197576, 6911871, 9999933, 8867531, 9617365, 5157165, 6999056, 9198602, 2608494, 9999933, 5940578, 2755723, 1548398, 3537278, 6756127, 2675175, 9999933, 8803686, 2708572, 7811557, 5552607, 824914, 4405171, 1558781, 1665038, 4099055, 1905832, 9999933, 3461618, 942595, 9576472, 9999933, 6413950, 4988151, 2623090, 2058807, 7435858, 529506, 9749080, 9635239, 8112420, 1004217, 14337, 461216, 357456, 1568883, 1611375, 570365, 1225683, 1094313, 3338646, 4146215, 6954748, 7027512, 6842764, 2889731, 4440665, 1527391, 1699890, 7487909, 1821814, 2055129, 3101791, 1615323, 9014571, 4141434, 3536021, 2657741, 9705217, 238221, 2438487, 513696, 5981868, 5482582, 830827, 1929964, 6810393]


print(birthdayCakeCandles(arr))

arr1 = [1, 2, 5, 1, 5, 3, 2, 4, 5, 1, 5, 5]
print(arr1.count(max(arr1)))
