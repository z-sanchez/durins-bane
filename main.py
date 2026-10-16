# Time Complexity: O(n), we traverse the array once max
# Space Complexity: O(1), no new data structure needed

def maxArea(input):

    result = 0

    left = 0
    right = len(input) - 1

    while left < right:
        maxArea = (right-left)*min(input[left], input[right])

        result = max(maxArea, result)

        if input[left] < input[right]:
            left += 1
        else:
            right -= 1

    return result


if "__main__" == __name__:
    input = [1, 7, 2, 5, 4, 7, 3, 6]
    result = maxArea(input)
    print(result)
