from typing import List


def dailyTemperatures(temps: int) -> List[str]:
    # default all to zero
    result = [0] * len(temps)
    stack = []

    # pair: [temp, index], this will keep track of temps we need to re-evaluate as we go down the list
    for index, temp in enumerate(temps):
        while stack and temp > stack[-1][0]:
            stackTemp, stackIndex = stack.pop()
            daysSince = index - stackIndex
            result[stackIndex] = daysSince
        stack.append([temp, index])
    # while our stack has values and the temp is greater than the top value
    # we must iterate through and evaluate prev temps waiting to be solved

    return result


if "__main__" == __name__:
    temperatures = [30, 38, 30, 36, 35, 40, 28]

    result = dailyTemperatures(temperatures)
    print(result)
