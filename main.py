

def containerWithMostWater(height):

    result = 0
    left = 0
    right = len(height) - 1

    while left < right:
        calculatedArea = (right - left) * min(height[left], height[right])
        result = max(result, calculatedArea)

        if left < right:
            left += 1
        else:
            right -= 1

    return result


if "__main__" == __name__:
    height = [1, 7, 2, 5, 4, 7, 3, 6]

    result = containerWithMostWater(height)
    print(result)
