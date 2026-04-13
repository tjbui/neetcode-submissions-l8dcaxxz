class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_rows, num_cols = len(grid), len(grid[0])

        num_islands = 0
        visited = set()
        q = deque()
        def bfs(row, col):
            q.append((row, col))
            visited.add((row, col))

            while q:
                curr_row, curr_col = q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for d_row, d_col in directions:
                    next_row, next_col = curr_row + d_row, curr_col + d_col
                    if ((next_row, next_col) not in visited and 
                        next_row in range(num_rows) and 
                        next_col in range(num_cols) and 
                        grid[next_row][next_col] == "1"
                       ):
                       q.append((next_row, next_col))
                       visited.add((next_row, next_col))
            
            return
        
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    num_islands += 1
                    bfs(row, col)

        return num_islands


# grid = [
#    ["1","1","0","0","1"],
#    ["1","1","0","0","1"],
#    ["0","0","1","0","0"],
#    ["0","0","0","1","1"]
#  ]

# Contain set of visited coordinates
# Run BFS on all 1's, adding visitable coordinates to visited set
# 

# (0, 0)
# visited: (0, 0), (0, 1), (1, 0), (1, 1) +1 island

# (2, 2)
# visited: (0, 0), (0, 1), (1, 0), (1, 1), (2, 2) +1 island

# 