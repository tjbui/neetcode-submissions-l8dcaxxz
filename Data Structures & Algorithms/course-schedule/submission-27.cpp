class Solution {
public:
    std::unordered_map<int, std::vector<int>> adjList{};
    std::unordered_set<int> visited{};

    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        for (int i = 0; i < numCourses; i++) {
            adjList[i] = {};
        }

        for (int i = 0; i < prerequisites.size(); i++) {
            adjList[prerequisites[i][0]].push_back(prerequisites[i][1]);
        }

        for (int course = 0; course < numCourses; course++) {
            if (!dfs(course)) {
                return false;
            }
        }

        return true;
    }

    bool dfs(int course) {
        if (adjList[course].empty()) {
            return true;
        }

        if (visited.contains(course)) {
            return false;
        }

        visited.insert(course);

        for (auto &node: adjList[course]) {
            if (!dfs(node)) {
                return false;
            }
        }

        visited.erase(course);
        adjList[course].clear();
        return true;
    }
};


// 0 --> 1
//   <--
// 