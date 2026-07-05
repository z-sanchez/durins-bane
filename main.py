# Time Complexity: O(n^2), we nest loops to traverse row and columns
# Space Complexity: O(n^2), each of our created mappings are two dimensional

def isValidSudoku(board):

    boxes = {}
    columns = {}
    rows = {}

    for row in range(9):
        for column in range(9):

            currentValue = board[row][column]

            if currentValue == ".":
                continue

            if row not in rows:
                rows[row] = []

            if column not in columns:
                columns[column] = []

            if (row//3, column//3) not in boxes:
                boxes[(row//3, column//3)] = []

            if currentValue in rows[row] or currentValue in columns[column] or currentValue in boxes[(row//3, column//3)]:
                return False

            rows[row].append(currentValue)
            columns[column].append(currentValue)
            boxes[(row//3, column//3)].append(currentValue)

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
