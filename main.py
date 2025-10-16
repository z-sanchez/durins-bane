# Time Complexity = O(n * logn) we use binary search with the while loop (logn) and the iterate (n) through the piles
# Space Complexity = O(1) no additional space needed
import math


def kokoBananas(piles, hours):

    left = 1
    right = max(piles)
    result = right

    while left <= right:
        midPoint = (right + left) // 2

        hoursCounted = 0
        for x in piles:
            hoursCounted += math.ceil(x/midPoint)

        if hoursCounted <= hours:
            right = midPoint - 1
            result = min(midPoint, result)
        else:
            left = midPoint + 1

    return result


if "__main__" == __name__:
    piles = [25, 10, 23, 4]
    hours = 4

    result = kokoBananas(piles, hours)
    print(result)
