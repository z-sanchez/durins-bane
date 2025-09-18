# Time Complexity = O(n) we traverse the array once
# Space Complexity = O(n) Need stack for potentially every index

def largestRectangleArea(heights) -> int:
    result = 0
    stack = []  # index, height

    for index, height in enumerate(heights):
        pointer = index

        while stack and height < stack[-1][1]:
            stackIndex, stackHeight = stack.pop()
            calculatedArea = stackHeight * (index - stackIndex)
            result = max(calculatedArea, result)
            pointer = stackIndex

        stack.append([pointer, height])

    for index, height in stack:
        calculatedArea = height * (len(heights) - index)
        result = max(result, calculatedArea)

    return result


if "__main__" == __name__:
    height = [7, 1, 7, 2, 2, 4]
    result = largestRectangleArea(height)
    print(result)
