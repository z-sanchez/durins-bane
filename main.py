# Time Complexity: O(n), we traverse the array once max
# Space Complexity: O(1), no new data structure needed

def maxArea(heights):

    left = 0
    right = len(heights) - 1
    result = 0

    while left < right:
        area = (right - left) * min(heights[left], heights[right])

        result = max(result, area)

        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1

    return result


if "__main__" == __name__:
    input = [1, 7, 2, 5, 4, 7, 3, 6]
    result = maxArea(input)
    print(result)
