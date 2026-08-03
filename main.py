# Time Complexity = O(n * logn) we use binary search with the while loop (logn) and the iterate (n) through the piles
# Space Complexity = O(1) no additional space needed
import math


def kokoBananas(piles, hours):

    left = 1
    right = max(piles)
    result = right

    while left <= right:
        bananasPerHour = (left + right) // 2

        timeToEat = 0
        for pile in piles:
            timeToEat += math.ceil(pile/bananasPerHour)

        if timeToEat <= hours:
            result = min(result, bananasPerHour)
            right = bananasPerHour - 1
        else:
            left = bananasPerHour + 1

    return result


if "__main__" == __name__:
    piles = [1, 4, 3, 2]
    hours = 9

    result = kokoBananas(piles, hours)
    print(result)
