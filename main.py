# Time Complexity: O(n^2), we nest loops to traverse row and columns
# Space Complexity: O(n^2), each of our created mappings are two dimensional

def isValidSudoku(board):
    # create hashmaps for each of the sections will need to check
    # boxes will store coordinates as the key (1-3 for row, 1-3 for column, total of nine boxes)
    boxes = {}
    columns = {}
    rows = {}

    for row in range(9):
        for column in range(9):
            currentValue = board[row][column]

            if currentValue == ".":
                continue

            if row not in rows:
                rows[row] = set()

            if column not in columns:
                columns[column] = set()

            if ((row//3), (column//3)) not in boxes:
                boxes[(row//3), (column//3)] = set()

            if currentValue in rows[row] or currentValue in columns[column] or currentValue in boxes[(row//3), (column//3)]:
                return False

            columns[column].add(currentValue)
            rows[row].add(currentValue)
            boxes[(row//3), (column//3)].add(currentValue)

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
