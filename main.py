import math


def isValidSudoku(board):
    boxes = {}
    rows = {}
    columns = {}

    for row in range(9):
        for column in range(9):
            value = board[row][column]

            if value == '.':
                continue

            if row not in rows:
                rows[row] = set()

            if column not in columns:
                columns[column] = set()

            if (row // 3, column // 3) not in boxes:
                boxes[(row // 3, column // 3)] = set()

            if value in rows[row] or value in columns[column] or value in boxes[(row // 3, column // 3)]:
                return False
            else:
                rows[row].add(value)
                columns[column].add(value)
                boxes[(row // 3, column // 3)].add(value)

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
