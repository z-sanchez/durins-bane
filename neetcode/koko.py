# Time Complexity = O(n * logn) we use binary search with the while loop (logn) and the iterate (n) through the piles
# Space Complexity = O(1) no additional space needed
import math


def kokoBananas(piles, hours):

    # our minimum speed is 1
    left = 1
    # our max speed to get the job done is the max banana count in the pile
    right = max(piles)
    # set to our max, as we use the algo, we'll compare found speeds to it
    result = right

    while left <= right:
        # imagine [min (left)....max (right)]
        # we're simply trying out the speeds between then will use binary search to decide which one to try next
        midpoint = (left + right) // 2

        hoursCounted = 0
        for x in piles:
            # banana amount / speed, ceil rounds up
            hoursCounted += math.ceil(x / midpoint)

        # if the eating speed can be eat all bananas in under the given time
        if hoursCounted <= hours:
            # turn result into our minimum speed required
            result = min(midpoint, result)
            # try out smaller speeds
            right = midpoint - 1
        else:
            # need more speed
            left = midpoint + 1

    return result


if "__main__" == __name__:
    piles = [25, 10, 23, 4]
    hours = 4

    result = kokoBananas(piles, hours)
    print(result)
