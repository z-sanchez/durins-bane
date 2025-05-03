# Time Complexity = O(n) we traverse the array once
# Space Complexity = O(1) No space needed

def trappedWater(heights):
    i = 0
    j = len(heights) - 1
    leftMax = heights[i]
    rightMax = heights[j]
    waterCount = 0

    while i < j:
        if leftMax < rightMax:
            i += 1
            leftMax = max(leftMax, heights[i])
            waterCount += leftMax - heights[i]
        else:
            j -= 1
            rightMax = max(rightMax, heights[j])
            waterCount += rightMax - heights[j]

    return waterCount


if "__main__" == __name__:
    heights = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
    result = trappedWater(heights)
    print(result)
