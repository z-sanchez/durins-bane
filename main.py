# Time Complexity: O((4^n)/sqrtN), I do not even know
# Space Complexity: O(n), we create the stack

from typing import List


def dailyTemperatures(temps: int) -> List[str]:
    result = []

    for index, value in enumerate(temps):
        print(index, value)

        daysUntil = 0
        x = index + 1
        while x < len(temps):
            if value < temps[x]:
                daysUntil = x - index
                break
            x += 1

        result.append(daysUntil)

    return result


if "__main__" == __name__:
    temperatures = [30, 38, 30, 36, 35, 40, 28]

    result = dailyTemperatures(temperatures)
    print(result)
