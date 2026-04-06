class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n_rows = len(heights)
        n_cols = len(heights[0])

        pacific_set = set()
        atlantic_set = set()

        def dfs(row, col, curr_set): # return true if can reach BOTH
            if (row, col) in curr_set:
                return

            curr_set.add((row, col))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc
                if (next_row in range(n_rows) and next_col in range(n_cols) and
                    heights[row][col] <= heights[next_row][next_col] and 
                   (next_row, next_col) not in curr_set):
                    curr_set.add((row, col))
                    dfs(next_row, next_col, curr_set)
                
            return        
            
        for i in range(n_cols):
            dfs(0, i, pacific_set)
            dfs(n_rows - 1, i, atlantic_set)
        for i in range(n_rows):
            dfs(i, 0, pacific_set)
            dfs(i, n_cols - 1, atlantic_set)

        result = []
        for i, j in pacific_set:
            if (i, j) in atlantic_set:
                result.append([i, j])

        return result
        


# heights = [
#  [4,2,7,3,4],
#  [7,4,6,4,7],
#  [6,3,5,3,6]
# ]

# DFS on all nodes --> if can reach [-1, X] or       [X, -1]
#                                           AND
#                                   [num_rows, X] or [X, num_cols]

#