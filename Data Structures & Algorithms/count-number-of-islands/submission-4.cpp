class Solution {
public:
    std::set<std::tuple<int, int>> visited{};
    int directions[4][2] = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};

    int numIslands(vector<vector<char>>& grid) {
        int numIslands{};

        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                std::tuple<int, int> node(i, j);

                if (!visited.contains(node) && grid[i][j] == '1') {
                    numIslands++;
                    bfs(grid, node);
                }
            }
        }

        return numIslands;
    }

    void bfs(vector<vector<char>>& grid, std::tuple<int, int> node) {
        std::deque<std::tuple<int, int>> neighbors{};

        neighbors.push_back(node);

        while (!neighbors.empty()) {
            std::tuple<int, int> nextNode = neighbors.front();
            neighbors.pop_front();

            if (visited.contains(nextNode)) continue;

            visited.insert(nextNode);
            int row = std::get<0>(nextNode);
            int col = std::get<1>(nextNode);

            for (auto &dir : directions) {
                std::tuple<int, int> neighbor(row + dir[0], col + dir[1]);

                if (row + dir[0] >= 0 && row + dir[0] < grid.size() &&
                        col + dir[1] >= 0 && col + dir[1] < grid[0].size() &&
                        !visited.contains(neighbor) && grid[row + dir[0]][col + dir[1]] == '1') {
                    
                    neighbors.push_back(neighbor);
                }
            }
        }
    }
};

// ["0", "1", "1", "1", "0"],
// ["0", "1", "0", "1", "0"],
// ["1", "1", "0", "0", "0"],
// ["0", "0", "0", "0", "0"]

//  visitedSet
//  BFS()
//    queue   
// 
//    while (queue contains nodes)
//      pop from queue
//
//      if visited(node)
//        continue
//      add to visited
//      add all neighbors (1) to queue
//      
//  numIslands()
//    
// 