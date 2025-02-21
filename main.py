
def isValidSudoku(board):
    boxes = []
    columns = []

    for currentColumn in range(9):
        column = []
        for currentRow in range(9):
            column.append(board[currentRow][currentColumn])
        columns.append(column)

    currentRowStart = 0
    currentColStart = 0

    # collects boxes
    while (currentColStart != 9):
        box = []

        for row in range(3):
            for col in range(3):
                box.append(board[currentColStart + col][currentRowStart + row])

        boxes.append(box)

        currentRowStart += 3

        if currentRowStart == 9:
            currentRowStart = 0
            currentColStart += 3

    for x in range(9):
        seen = []

        for i in range(9):
            value = boxes[x][i]

            if (value != "." and value in seen):
                return False
            else:
                seen.append(value)

    for x in range(9):
        seen = []

        for i in range(9):
            value = board[x][i]

            if (value != "." and value in seen):
                return False
            else:
                seen.append(value)

    for x in range(9):
        seen = []

        for i in range(9):
            value = columns[x][i]

            if (value != "." and value in seen):
                return False
            else:
                seen.append(value)

    return True


if __name__ == "__main__":
    board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
             ["4", ".", ".", "5", ".", ".", ".", ".", "."],
             [".", "9", "1", ".", ".", ".", ".", ".", "3"],
             ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
             [".", ".", ".", "8", ".", "3", ".", ".", "5"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", ".", ".", ".", ".", ".", "2", ".", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "8"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(isValidSudoku(board))
