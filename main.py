from typing import List


def dailyTemperatures(temps: int) -> List[str]:
    # default all to zero
    result = [0] * len(temps)

    stack = []  # index, temp

    for index, temp in enumerate(temps):
        while stack and stack[-1][1] < temp:
            stackIndex, stackTemp = stack.pop()
            result[stackIndex] = index - stackIndex
        stack.append([index, temp])

    return result


if "__main__" == __name__:
    temperatures = [30, 38, 30, 36, 35, 40, 28]

    result = dailyTemperatures(temperatures)
    print(result)
