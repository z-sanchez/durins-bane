# Time Complexity = O(n) we traverse the array once
# Space Complexity = O(1) No space needed

def trappingRainwater(height):

    if not height:
        return 0

    left = 0
    right = len(height) - 1
    leftMax = height[left]
    rightMax = height[right]
    result = 0

    while left < right:
        if leftMax < rightMax:
            left += 1
            leftMax = max(leftMax, height[left])
            result += leftMax - height[left]
        else:
            right -= 1
            rightMax = max(rightMax, height[right])
            result += rightMax - height[right]

    return result


if "__main__" == __name__:
    height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
    result = trappingRainwater(height)
    print(result)
