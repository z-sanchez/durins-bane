# Time Complexity = O(n) we traverse the array once
# Space Complexity = O(n) Need stack for potentially every index

def largestRectangleArea(heights) -> int:
    maxArea = 0
    stack = []  # index, height

    for index, height in enumerate(heights):
        pointerIndex = index
        while stack and height < stack[-1][1]:
            stackIndex, stackHeight = stack.pop()

            maxArea = max(maxArea, stackHeight * (index - stackIndex))
            pointerIndex = stackIndex
        stack.append([pointerIndex, height])

    for index, height in stack:
        maxArea = max(maxArea, height * (len(heights) - index))

    return maxArea


if "__main__" == __name__:
    height = [7, 1, 7, 2, 2, 4]
    result = largestRectangleArea(height)
    print(result)
