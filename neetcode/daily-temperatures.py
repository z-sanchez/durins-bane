from typing import List


def dailyTemperatures(temps: int) -> List[str]:
    # default all to zero
    result = [0] * len(temps)

    # pair: [temp, index], this will keep track of temps we need to re-evaluate as we go down the list
    stack = []

    for index, temperature in enumerate(temps):
        # while our stack has values and the temp is greater than the top value
        # we must iterate through and evaluate prev temps waiting to be solved
        while stack and temperature > stack[-1][0]:
            stackTemp, stackIndex = stack.pop()
            result[stackIndex] = index - stackIndex  # days until warmer temp
        stack.append([temperature, index])

    return result


if "__main__" == __name__:
    temperatures = [30, 38, 30, 36, 35, 40, 28]

    result = dailyTemperatures(temperatures)
    print(result)
