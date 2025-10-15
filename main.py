from typing import List


def dailyTemperatures(temps: int) -> List[str]:
    # default all to zero
    result = [0] * len(temps)

    stack = []
    # pair: [temp, index], this will keep track of temps we need to re-evaluate as we go down the list

    for index, temp in enumerate(temps):

        while stack and stack[-1][1] < temp:
            prevIndex, prevTemp = stack.pop()
            result[prevIndex] = index - prevIndex

        stack.append([index, temp])

    return result


if "__main__" == __name__:
    temperatures = [30, 38, 30, 36, 35, 40, 28]

    result = dailyTemperatures(temperatures)
    print(result)
