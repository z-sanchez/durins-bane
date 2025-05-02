def isValidSudoku(input):
    output = True

    rows = {}
    columns = {}
    boxes = {}

    for r in range(9):
        for c in range(9):
            if input[r][c] == ".":
                continue

            if r not in rows:
                rows[r] = set()

            if c not in columns:
                columns[c] = set()

            if (r//3, c//3) not in boxes:
                boxes[(r//3, c//3)] = set()

            if (input[r][c] in rows[r] or input[r][c] in columns[c] or input[r][c] in boxes[(r//3, c//3)]):
                return False

            rows[r].add(input[r][c])
            columns[c].add(input[r][c])
            boxes[((r//3, c//3))].add(input[r][c])

    return output


if "__main__" == __name__:

    board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
             ["4", ".", ".", "5", ".", ".", ".", ".", "."],
             [".", "9", "1", ".", ".", ".", ".", ".", "3"],
             ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
             [".", ".", ".", "8", ".", "3", ".", ".", "5"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", ".", ".", ".", ".", ".", "2", ".", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "8"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    result = isValidSudoku(board)

    print("Is Valid Sudoku: ", result)
