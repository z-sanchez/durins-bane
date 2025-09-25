def searchMatrix(matrix, target):
    ROWS = len(matrix)  # get length of outer list
    COLS = len(matrix[0])  # get length of inner list

    # start like usual binary search
    left = 0
    right = ROWS - 1

    while left <= right:
        # midpoint is the middle row
        middleRow = (left + right) // 2

        # regular binary search logic with the twist
        # we are checking the begin and end of the list
        if target > matrix[middleRow][-1]:
            left = middleRow + 1
        elif target < matrix[middleRow][0]:
            right = middleRow - 1
        else:
            break

    # it's possible our adjusted pointers are out of range, so check it
    if not (left <= right):
        return False

    # restart but on the inner list level
    left = 0
    right = COLS - 1

    # normal binary search
    while left <= right:
        midPoint = midPoint = (left + right) // 2

        # use middleRow we found from earlier to look at the right row
        if target > matrix[middleRow][midPoint]:
            left = midPoint + 1
        elif target < matrix[middleRow][midPoint]:
            right = midPoint - 1
        else:
            return True

    return False


if "__main__" == __name__:
    matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]]
    target = 12
    result = searchMatrix(matrix, target)
    print(result)
