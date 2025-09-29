# Time Complexity = O(n) we traverse the array once
# Space Complexity = O(1) No space needed

def trappingRainwater(height):

    if not height:
        return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]

    result = 0

    while l < r:

        if leftMax < rightMax:
            l += 1
            leftMax = max(height[l], leftMax)
            result += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            result += rightMax - height[r]

    return result


if "__main__" == __name__:
    height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
    result = trappingRainwater(height)
    print(result)
