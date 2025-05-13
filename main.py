# Time Complexity: O(n), we traverse the array once max
# Space Complexity: O(n), we create the stack

from typing import List


def containerWithMostWater(heights: List[str]) -> int:

    if not heights:
        return 0

    result = 0
    left = 0
    right = len(heights) - 1

    while left < right:
        calculatedArea = (right - left) * min(heights[left], heights[right])
        result = max(calculatedArea, result)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return result


if "__main__" == __name__:
    input = [2, 2, 2]
    result = containerWithMostWater(input)
    print(result)
