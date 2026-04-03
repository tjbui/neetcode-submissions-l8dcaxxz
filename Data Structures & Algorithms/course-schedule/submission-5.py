class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        visited = set()

        # dfs and return False if detect cycle (can't complete that course)
        def dfs(course): 
            if preMap[course] == []:
                return True
            if course in visited:
                return False

            visited.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            
            visited.remove(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
            
        
        

# numCourses = 2, prerequisites = [[0,1],[1,0]]
# {0: [1], 1: [0]}

# 0 --> 1
#   <--
