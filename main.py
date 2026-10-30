import math


def searchMatrix(matrix, target):
    OUTER_LENGTH = len(matrix)
    INNER_LENGTH = len(matrix[0])

    outerLow = 0
    outerHigh = OUTER_LENGTH - 1

    while outerLow <= outerHigh:
        outerMidpoint = (outerHigh + outerLow) // 2

        if matrix[outerMidpoint][0] > target:
            outerHigh = outerMidpoint - 1
        elif matrix[outerMidpoint][-1] < target:
            outerLow = outerMidpoint + 1
        else:
            break

    if not outerLow <= outerHigh:
        return False

    innerLow = 0
    innerHigh = INNER_LENGTH - 1

    while innerLow <= innerHigh:
        innerMidpoint = (innerLow + innerHigh) // 2

        if matrix[outerMidpoint][innerMidpoint] < target:
            innerLow = innerMidpoint + 1
        elif matrix[outerMidpoint][innerMidpoint] > target:
            innerHigh = innerMidpoint - 1
        else:
            return True

    return False


if "__main__" == __name__:
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    result = searchMatrix(matrix, target)
    print(result)
