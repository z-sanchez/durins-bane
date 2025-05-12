# Time Complexity = O(1) we never traverse, constant time for everything
# Space Complexity = O(n) create stacks

def containerWithMostWater(heights):

    result = 0

    left = 0
    right = len(heights) - 1

    while left < right:
        area = (right - left) * min(heights[left], heights[right])
        result = max(area, result)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return result


if "__main__" == __name__:
    heights = [2, 2, 2]
    result = containerWithMostWater(heights)
    print(result)
