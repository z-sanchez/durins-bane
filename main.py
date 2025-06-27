def isValidSudoku(board):
    boxes = {}
    columns = {}
    rows = {}

    for row in range(9):
        for column in range(9):
            currentSquare = board[row][column]

            if currentSquare == ".":
                continue

            if row not in rows:
                rows[row] = set()

            if column not in columns:
                columns[column] = set()

            print(column)
            print(row//3, column//3)

            if (row//3, column//3) not in boxes:
                boxes[(row//3, column//3)] = set()

            if currentSquare in rows[row] or currentSquare in columns[column] or currentSquare in boxes[(row//3, column//3)]:
                return False

            rows[row].add(currentSquare)
            columns[column].add(currentSquare)
            boxes[(row//3, column//3)].add(currentSquare)

    return True


if __name__ == "__main__":
    board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
             ["4", ".", ".", "5", ".", ".", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", ".", "3"],
             ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
             [".", ".", ".", "8", ".", "3", ".", ".", "5"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", ".", ".", ".", ".", ".", "2", ".", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "8"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


print(isValidSudoku(board))
