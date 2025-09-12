# Time Complexity = O(n) we traverse the array once
# Space Complexity = O(n) Need stack for potentially every index

def largestRectangleArea(heights) -> int:

    maxArea = 0
    stack = []  # pair: (index, height)

    for index, height in enumerate(heights):
        currentIndex = index

        # pop and calc area if the previous height is greater (their time of being a rectangle has come to an end)
        # the loop will stop at the point where the shape is still possible
        while stack and stack[-1][1] > height:
            prevIndex, prevHeight = stack.pop()

            # current wall position - previous taller wall = width of rectangle
            maxArea = max(maxArea, prevHeight * (index - prevIndex))

            # this is for later
            currentIndex = prevIndex

        # keep track of how far the current (index) wall can go back
        stack.append((currentIndex, height))

    for index, height in stack:
        # these made it all the way to the end as rectangles so calculate the remaining max areas
        # len(heights) = total width of the chart
        maxArea = max(maxArea, height * (len(heights) - index))

    return maxArea


if "__main__" == __name__:
    height = [7, 1, 7, 2, 2, 4]
    result = largestRectangleArea(height)
    print(result)
