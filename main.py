def searchMatrix(matrix, target):

    left = 0
    right = len(matrix) - 1

    while left <= right:
        midpoint = left + (right - left) // 2
        print(midpoint)

        first = matrix[midpoint][0]
        last = matrix[midpoint][-1]

        if (target <= last and target >= first):
            for x in matrix[midpoint]:
                if x == target:
                    return True
            return False
        elif target > first:
            left = midpoint + 1
        else:
            right = midpoint - 1

    return False


if "__main__" == __name__:
    matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
    target = 22
    result = searchMatrix(matrix, target)
    print(result)
