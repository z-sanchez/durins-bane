
def isValidSudoku(board):
    boxes = {}
    columns = {}
    rows = {}

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue

            if c not in columns:
                columns[c] = set()

            if r not in rows:
                rows[r] = set()

            if (r//3, c//3) not in boxes:
                boxes[(r//3, c//3)] = set()

            if (board[r][c] in columns[c] or
                    board[r][c] in rows[r] or
                    board[r][c] in boxes[(r//3, c//3)]):
                return False

            columns[c].add(board[r][c])
            rows[r].add(board[r][c])
            boxes[r//3, c//3].add(board[r][c])

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
