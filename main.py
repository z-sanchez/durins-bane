# Time Complexity: O(n), we traverse the array once max
# Space Complexity: O(1), no new data structure needed

def maxArea(heights):
    result = 0
    left = 0
    right = len(heights) - 1

    while left < right:
        calculatedArea = (right - left) * min(heights[left], heights[right])
        result = max(result, calculatedArea)

        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1

    return result


if "__main__" == __name__:
    input = [1, 7, 2, 5, 4, 7, 3, 6]
    result = maxArea(input)
    print(result)
