from typing import List


def dailyTemperatures(temps: int) -> List[str]:
    # default all to zero
    result = [0] * len(temps)

    stack = []

    for index, temp in enumerate(temps):
        while stack and temp > stack[-1][0]:
            stackTemp, stackIndex = stack.pop()
            result[stackIndex] = index - stackIndex
        stack.append([temp, index])

    return result


if "__main__" == __name__:
    temperatures = [30, 38, 30, 36, 35, 40, 28]
    test = []
    result = dailyTemperatures(temperatures)
    print(result)
    print(bool(test))
    print(bool(temperatures))
