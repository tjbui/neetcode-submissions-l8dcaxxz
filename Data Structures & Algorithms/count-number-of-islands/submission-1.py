from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0

        num_islands = 0
        visited = set()
        num_rows = len(grid)
        num_cols = len(grid[0])

        def bfs(row, col):
            q = deque()

            q.append((row, col))
            visited.add((row, col))
            while q:
                curr_row, curr_col = q.popleft()

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    if ((curr_row + dr in range(num_rows)) and
                       (curr_col + dc in range(num_cols)) and
                       ((curr_row + dr, curr_col + dc) not in visited) and
                       (grid[curr_row + dr][curr_col + dc] == "1")):
                       visited.add((curr_row + dr, curr_col + dc))
                       q.append((curr_row + dr, curr_col + dc))

        for i in range(num_rows):
            for j in range(num_cols):
                if (grid[i][j] == "1" and (i, j) not in visited):
                    bfs(i, j)
                    num_islands += 1

        return num_islands

# grid = [
#    ["1","1","0","0","1"],
#    ["1","1","0","0","1"],
#    ["0","0","1","0","0"],
#    ["0","0","0","1","1"]
#  ]