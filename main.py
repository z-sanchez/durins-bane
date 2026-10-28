import math


def dailyTemperatures(temperatures):

    result = [0 for x in range(len(temperatures))]

    stack = []  # index, temp

    for index, temp in enumerate(temperatures):
        while stack and stack[-1][1] < temp:
            stackIndex, stackTemp = stack.pop()
            result[stackIndex] = index - stackIndex
        stack.append([index, temp])

    return result


if "__main__" == __name__:
    temperatures = [30, 38, 30, 36, 35, 40, 28]

    result = dailyTemperatures(temperatures)
    print(result)
