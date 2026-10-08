# Time Complexity: O(n^2), we nest loops to traverse row and columns
# Space Complexity: O(n^2), each of our created mappings are two dimensional

def isValidSudoku(board):
    # create hashmaps for each of the sections will need to check
    # boxes will store coordinates as the key (1-3 for row, 1-3 for column, total of nine boxes)
    boxes = {}
    columns = {}
    rows = {}

    for row in range(9):
        for col in range(9):
            square = board[row][col]

            if square == '.':
                continue

            if row not in rows:
                rows[row] = set()

            if col not in columns:
                columns[col] = set()

            if (row//2, col//2) not in boxes:
                boxes[(row//2, col//2)] = set()

            if square in rows[row] or square in columns[col] or square in boxes[(row//2, col//2)]:
                return False

            rows[row].add(square)
            columns[col].add(square)
            boxes[(row//2, col//2)].add(square)

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
