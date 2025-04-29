def maxArea(heights):
    i = 0
    j = i + 1
    result = 0

    while i < len(heights):
        while j < len(heights):
            calculation = (len(heights[i:j])) * min(heights[i], heights[j])
            result = max(result, calculation)
            j += 1
        i += 1
        j = i + 1

    return result


if "__main__" == __name__:
    input = [2, 2, 2]
    result = maxArea(input)
    print(result)
