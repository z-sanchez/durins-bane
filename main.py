def searchMatrix(matrix, target):
    ROWS = len(matrix)
    COLS = len(matrix[0])

    left = 0
    right = ROWS - 1

    while left <= right:
        midpoint = (right + left) // 2

        if matrix[midpoint][0] > target:
            right = midpoint - 1
        elif matrix[midpoint][-1] < target:
            left = midpoint + 1
        else:
            break

    if not left <= right:
        return False

    row = midpoint
    left = 0
    right = COLS - 1

    while left <= right:
        midpoint = (right + left) // 2

        if matrix[row][midpoint] > target:
            right = midpoint - 1
        elif matrix[row][midpoint] < target:
            left += 1
        else:
            return True

    return False


if "__main__" == __name__:
    matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
    target = 12
    result = searchMatrix(matrix, target)
    print(result)
