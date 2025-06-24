

def dailyTemperatures(temps):
    result = [0] * len(temperatures)
    stack = []

    for index, temp in enumerate(temps):
        while stack and temp > stack[-1][0]:
            stackTemp, stackIndex = stack.pop()
            result[stackIndex] = index - stackIndex
        stack.append([temp, index])

    return result


if "__main__" == __name__:
    temperatures = [30, 38, 30, 36, 35, 40, 28]

    result = dailyTemperatures(temperatures)
    print(result)
