from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0
        visited = set()
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                curr_r, curr_c = q.popleft()
                #visited.add(curr_r, curr_c)

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions: # all neighbors of curr_r, curr_c
                    if (((curr_r + dr) in range(rows)) and
                        ((curr_c + dc) in range(cols)) and
                        (grid[curr_r + dr][curr_c + dc] == "1") and
                        (curr_r + dr, curr_c + dc) not in visited):
                        visited.add((curr_r + dr, curr_c + dc))
                        q.append((curr_r + dr, curr_c + dc))

        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == "1") and ((r, c) not in visited):
                    bfs(r, c)
                    num_islands += 1

        return num_islands

# grid = [
#    ["1","1","0","0","1"],
#    ["1","1","0","0","1"],
#    ["0","0","1","0","0"],
#    ["0","0","0","1","1"]
#  ]

# 