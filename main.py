# Time Complexity: O(n^2), we nest loops to traverse row and columns
# Space Complexity: O(n^2), each of our created mappings are two dimensional

def isValidSudoku(board):

    columns = {}
    rows = {}
    boxes = {}

    for row in range(9):
        for column in range(9):
            currentSquare = board[row][column]

            if currentSquare == '.':
                continue

            if column not in columns:
                columns[column] = set()

            if row not in rows:
                rows[row] = set()

            if (row//3, column // 3) not in boxes:
                boxes[(row//3, column // 3)] = set()

            if currentSquare in columns[column] or currentSquare in rows[row] or currentSquare in boxes[(row//3, column // 3)]:
                return False

            columns[column].add(currentSquare)
            rows[row].add(currentSquare)
            boxes[(row//3, column // 3)].add(currentSquare)

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
