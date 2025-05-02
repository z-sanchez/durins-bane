def containerWithMostWater(heights):

    result = 0

    i = 0
    j = len(heights) - 1

    while i < j:
        currentArea = min(heights[i], heights[j]) * (j - i)
        result = max(currentArea, result)

        if heights[i] < heights[j]:
            i += 1
        elif heights[j] < heights[i]:
            j -= 1
        else:
            i += 1

    return result


if "__main__" == __name__:

    heights = [2, 2, 2]

    result = containerWithMostWater(heights)

    print("Correct: ", result == 36)
    print("You answered: ", result)
