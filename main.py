# Time Complexity = O(n) we traverse the array once
# Space Complexity = O(n) Need stack for potentially every index

def largestRectangleArea(heights) -> int:

    maxArea = 0
    stack = []  # pair: (index, height)

    for index, height in enumerate(heights):
        pointer = index

        while stack and height < stack[-1][1]:
            stackIndex, stackHeight = stack.pop()
            calculatedArea = (index - stackIndex) * stackHeight
            maxArea = max(calculatedArea, maxArea)
            pointer = stackIndex
        stack.append([pointer, height])

    for index, height in stack:
        calculatedArea = (len(heights) - index) * height
        maxArea = max(calculatedArea, maxArea)

    return maxArea


if "__main__" == __name__:
    height = [7, 1, 7, 2, 2, 4]
    result = largestRectangleArea(height)
    print(result)
