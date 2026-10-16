# Time Complexity: O(n), we traverse the array once max
# Space Complexity: O(1), no new data structure needed


def dailyTemperatures(temperatures):

    result = [0] * len(temperatures)
    stack = []

    for index, temp in enumerate(temperatures):
        while len(stack) > 0 and stack[-1][1] < temp:
            poppedIndex, poppedStack = stack.pop()
            result[poppedIndex] = index - poppedIndex
        stack.append([index, temp])

    return result


if "__main__" == __name__:
    temperatures = [30, 38, 30, 36, 35, 40, 28]

    result = dailyTemperatures(temperatures)
    print(result)
