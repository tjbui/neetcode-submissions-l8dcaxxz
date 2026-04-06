class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            for neighbor in adjList[node]:
                if neighbor != parent:
                    if not dfs(neighbor, node):
                        return False

            return True

        return dfs(0, None) and len(visited) == n
        

# tree is undirected, acyclic, connected graph

# n = 5
# edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

#      3 -- 0 -- 1 -- 4
#           |
#           2

# create adjacency list, check if cycle 
# { 
#   0 --> [1, 2, 3] 
#   1 --> [0, 4]
#   2 --> [0]
#   3 --> [0]
#   4 --> [1]
# }


# n = 5
# edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

#           ----------------
#           |              |
#      0 -- 1 -- 2 -- 3 -- 4
#           |         |
#           -----------