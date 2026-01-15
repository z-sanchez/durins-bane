from typing import List


def dailyTemperatures(temps: int) -> List[str]:
    result = [0] * len(temps)

    stack = []  # temp, index

    for index, temperature in enumerate(temps):
        while stack and temperature > stack[-1][0]:
            stackTemp, stackIndex = stack.pop()
            result[stackIndex] = index - stackIndex
        stack.append([temperature, index])

    return result


if "__main__" == __name__:
    temperatures = [30, 38, 30, 36, 35, 40, 28]

    result = dailyTemperatures(temperatures)
    print(result)
