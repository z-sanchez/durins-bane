# Time Complexity: O(n^2), we nest loops to traverse row and columns
# Space Complexity: O(n^2), each of our created mappings are two dimensional

def isValidSudoku(board):
    # create hashmaps for each of the sections will need to check
    # boxes will store coordinates as the key (1-3 for row, 1-3 for column, total of nine boxes)
    boxes = {}
    columns = {}
    rows = {}

    # iterate row first
    for r in range(9):
        # iterate through columns
        for c in range(9):
            # ignore this
            if board[r][c] == ".":
                continue

            # making their default into sets
            if c not in columns:
                columns[c] = set()

            if r not in rows:
                rows[r] = set()

            # calculating box coordinate
            if (r//3, c//3) not in boxes:
                boxes[(r//3, c//3)] = set()

            # if the current node exist in either of the maps
            if (board[r][c] in columns[c] or
                    board[r][c] in rows[r] or
                    board[r][c] in boxes[(r//3, c//3)]):
                return False

            # else, we just add it to the appropriate maps
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
