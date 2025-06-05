

def dailyTemperatures(temp):
    result = [0] * len(temp)
    stack = []

    for index, value in enumerate(temp):
        while stack and value > stack[-1][0]:
            stackTemp, stackIndex = stack.pop()
            result[stackIndex] = index - stackIndex
        stack.append([value, index])

    return result


if "__main__" == __name__:
    temperatures = [30, 38, 30, 36, 35, 40, 28]

    result = dailyTemperatures(temperatures)
    print(result)
