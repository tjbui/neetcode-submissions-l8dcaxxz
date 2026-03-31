class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check each row
        for row in board:
            s = set()
            for digit in row:
                if digit in s:
                    return False
                if digit != ".":
                    s.add(digit)

        # check each column
        for col in range(0, 9):
            s = set()
            for i in range(0, 9):
                if board[i][col] in s:
                    return False
                if board[i][col] != ".":
                    s.add(board[i][col])

        # check 3x3
        for i in range(0, 3):
            for j in range(0, 3):
                s = set()
                for k in range(0, 3):
                    if board[i * 3 + 0][j * 3 + k] in s:
                        return False
                    if board[i * 3 + 0][j * 3 + k] != ".":
                        s.add(board[i * 3 + 0][j * 3 + k])
                    
                    if board[i * 3 + 1][j * 3 + k] in s:
                        return False
                    if board[i * 3 + 1][j * 3 + k] != ".":
                        s.add(board[i * 3 + 1][j * 3 + k])

                    if board[i * 3 + 2][j * 3 + k] in s:
                        return False
                    if board[i * 3 + 2][j * 3 + k] != ".":
                        s.add(board[i * 3 + 2][j * 3 + k])
                
        return True
                

# board[0][0], board[0][1], board[0][2]
# board[1][0], board[1][1], board[1][2]
# board[2][0], board[2][1], board[2][2]

# board[3][0], board[3][1], board[3][2]
# board[4][0], board[4][1], board[4][2]
# board[5][0], board[5][1], board[5][2]
         

# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]


# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]