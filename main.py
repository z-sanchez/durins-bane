import math


def kokoBananas(piles, hours):
    low = 1
    high = max(piles)

    result = high

    while low <= high:
        midpoint = (low + high) // 2

        hoursToEat = 0

        for bananas in piles:
            hoursToEat += math.ceil(bananas/midpoint)

        if hoursToEat <= hours:
            high = midpoint - 1
            result = min(midpoint, result)
        else:
            low = midpoint + 1

    return result


if "__main__" == __name__:
    piles = [25, 10, 23, 4]
    hours = 4

    result = kokoBananas(piles, hours)
    print(result)
