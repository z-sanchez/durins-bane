# Time Complexity = O(n) we traverse the array once
# Space Complexity = O(n) Need stack for potentially every index

def largestRectangleArea(heights) -> int:

    maxArea = 0
    stack = []  # index, height

    for index, height in enumerate(heights):
        currentIndex = index

        while stack and stack[-1][1] > height:
            stackIndex, stackHeight = stack.pop()
            maxArea = max(maxArea, stackHeight * (index - stackIndex))
            currentIndex = stackIndex
        stack.append([currentIndex, height])

    for index, height in stack:
        maxArea = max(maxArea, (len(heights) - index) * height)

    return maxArea


if "__main__" == __name__:
    height = [7, 1, 7, 2, 2, 4]
    result = largestRectangleArea(height)
    print(result)
