class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}
        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)

        num_components = 0
        visited = set()

        def dfs(n, parent):
            if n in visited:
                return False

            visited.add(n)
            for neighbor in adjList[n]:
                if neighbor != parent:
                    dfs(neighbor, n)
            return True

        for i in range(n):
            if dfs(i, None):
                num_components += 1

        return num_components
