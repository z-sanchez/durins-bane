# Time Complexity: O(n), we traverse the array once max
# Space Complexity: O(1), no new data structure needed

def maxArea(heights):
    left = 0
    right = len(heights) - 1
    result = 0

    while left < right:
        calculatedArea = (right - left) * min(heights[right], heights[left])

        result = max(calculatedArea, result)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return result


if "__main__" == __name__:
    input = [1, 7, 2, 5, 4, 7, 3, 6]
    result = maxArea(input)
    print(result)
