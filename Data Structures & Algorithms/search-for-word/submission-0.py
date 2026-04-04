class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n_rows, n_cols = len(board), len(board[0])
        path = set()

        def dfs(row, col, curr_str):
            if (row >= n_rows or row < 0 or
                col >= n_cols or col < 0 or
                (row, col) in path):
                return False

            ch = board[row][col]
            curr_str += ch
            if curr_str == word:
                return True

            path.add((row, col))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for d_row, d_col in directions:
                if dfs(row + d_row, col + d_col, curr_str):
                    return True
            path.remove((row, col))

            return False

        for i in range(n_rows):
            for j in range(n_cols):
                if dfs(i, j, ""):
                    return True
        return False

#  [
#   ["A","B","C","D"],
#   ["S","A","A","T"],
#   ["A","C","A","E"]
#  ]
