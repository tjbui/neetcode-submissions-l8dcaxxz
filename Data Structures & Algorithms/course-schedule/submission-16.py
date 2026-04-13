class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        
        visited = set()
        def dfs(course):
            if preMap[course] == []:
                return True # Can be completed

            visited.add(course)
            for prereq in preMap[course]:
                if prereq in visited:
                    return False
                if not dfs(prereq):
                    return False
            preMap[course] = []
            visited.remove(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
# 
# 
# 0 --> 1 --> 2 --> 3
#   <--------
#
# 
# Run dfs on all nodes, if we revisit the same nodeat any point, there is a cycle

# {
#   0: [1]
#   1: [2]
#   2: [1, 3]
#   3: []
# }


# 3 --> 1 --> 4
# | 
# v
# 2 --> 4
#