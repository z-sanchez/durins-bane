
def searchMatrix(matrix, target):
    OUTER_LENGTH = len(matrix)
    INNER_LENGTH = len(matrix[0])

    outerLow = 0
    outerHigh = OUTER_LENGTH - 1

    while outerLow <= outerHigh:
        outerMidpoint = (outerLow + outerHigh) // 2

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
        innerMidpoint = (innerHigh + innerLow)//2

        if matrix[outerMidpoint][innerMidpoint] < target:
            innerLow = innerMidpoint + 1
        elif matrix[outerMidpoint][innerMidpoint] > target:
            innerHigh = innerMidpoint - 1
        else:
            return True

    return False


if "__main__" == __name__:
    matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
    target = 12
    result = searchMatrix(matrix, target)
    print(result)
