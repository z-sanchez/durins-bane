

def largestRectangleArea(heights):

    result = 0
    stack = []  # index, height

    for index, height in enumerate(heights):

        pointer = index

        while stack and stack[-1][1] > height:
            stackIndex, stackHeight = stack.pop()
            calculatedArea = (index - stackIndex) * stackHeight
            result = max(result, calculatedArea)
            pointer = stackIndex

        stack.append([pointer, height])

    for index, height in stack:
        calculatedArea = (len(heights) - index) * height
        result = max(calculatedArea, result)

    return result


if "__main__" == __name__:
    height = [7, 1, 7, 2, 2, 4]
    result = largestRectangleArea(height)
    print(result)
