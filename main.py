# Time Complexity: O(n), we traverse the array once max
# Space Complexity: O(1), no new data structure needed


def isValidSudoku(board):
    rows = {}
    columns = {}
    boxes = {}

    for row in range(9):
        for column in range(9):

            node = board[row][column]

            if node == ".":
                continue

            if row not in rows:
                rows[row] = set()

            if column not in columns:
                columns[column] = set()

            if (row//3, column//3) not in boxes:
                boxes[(row//3, column//3)] = set()

            if node in rows[row] or node in columns[column] or node in boxes[(row//3, column//3)]:
                return False
            else:
                rows[row].add(node)
                columns[column].add(node)
                boxes[(row//3, column//3)].add(node)

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
