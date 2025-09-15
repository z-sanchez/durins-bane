# Time Complexity = O(n) we traverse the array once
# Space Complexity = O(n) Need stack for potentially every index

def largestRectangleArea(heights) -> int:

    maxArea = 0
    stack = []  # index, height

    for index, height in enumerate(heights):
        pointerIndex = index
        while stack and stack[-1][1] > height:
            prevIndex, prevHeight = stack.pop()
            maxArea = max(maxArea, prevHeight * (index - prevIndex))
            pointerIndex = prevIndex

        stack.append([pointerIndex, height])

    for index, height in stack:
        maxArea = max(maxArea, height * (len(heights) - index))

    return maxArea


if "__main__" == __name__:
    height = [7, 1, 7, 2, 2, 4]
    result = largestRectangleArea(height)
    print(result)
