# Time Complexity = O(n * logn) we use binary search with the while loop (logn) and the iterate (n) through the piles
# Space Complexity = O(1) no additional space needed
import math


def kokoBananas(piles, hours):

    left = 0
    right = max(piles)

    result = right

    while left <= right:
        bph = (right+left) // 2

        hoursCounted = 0

        for x in piles:
            hoursCounted += math.ceil(x/bph)

        if hoursCounted <= hours:
            result = min(result, bph)
            right = bph - 1
        else:
            left = bph + 1

    return result


if "__main__" == __name__:
    piles = [25, 10, 23, 4]
    hours = 4

    result = kokoBananas(piles, hours)
    print(result)
