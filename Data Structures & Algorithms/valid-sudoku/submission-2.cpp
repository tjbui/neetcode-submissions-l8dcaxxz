class Solution {
public:
    bool validBox(int row_0, int col_0, vector<vector<char>>& board) {
        std::unordered_set<char> box_set{};

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[row_0 + i][col_0 + j] == '.') {
                    continue;
                }
                if (box_set.contains(board[row_0 + i][col_0 + j])) {
                    return false;
                }

                box_set.insert(board[row_0 + i][col_0 + j]);
            }
        }

        return true;
    }

    bool isValidSudoku(vector<vector<char>>& board) {
        std::unordered_set<char> row_set{}, col_set{};

        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[0].size(); j++) {
                if (board[i][j] == '.') {
                    continue;
                }

                if (row_set.contains(board[i][j])) {
                    return false;
                }
                row_set.insert(board[i][j]);
            }
            row_set.clear();
        }

        for (int i = 0; i < board[0].size(); i++) {
            for (int j = 0; j < board.size(); j++) {
                if (board[j][i] == '.') {
                    continue;
                }
                
                if (col_set.contains(board[j][i])) {
                    return false;
                }
                col_set.insert(board[j][i]);
            }
            col_set.clear();
        }

        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (!validBox(3 * i, 3 * j, board)) {
                    return false;
                }
            }
        }

        return true;
    }
};

// [["1","2",".",".","3",".",".",".","."],
//  ["4",".",".","5",".",".",".",".","."],
//  [".","9","8",".",".",".",".",".","3"],
//  ["5",".",".",".","6",".",".",".","4"],
//  [".",".",".","8",".","3",".",".","5"],
//  ["7",".",".",".","2",".",".",".","6"],
//  [".",".",".",".",".",".","2",".","."],
//  [".",".",".","4","1","9",".",".","8"],
//  [".",".",".",".","8",".",".","7","9"]]

// for each row:
// add to all numbers to an unordered_set. If duplicate, invald

// for each column:
// add to all numbers to an unordered_set. If duplicate, invald

// for each 3x3 square:
// add all numnbers to an unordered_set. If duplicate, invalid


// i = 0, j = 0
// (0, 0), (0, 1), (0, 2)
// (1, 0), (1, 1), (1, 2)
// (2, 0), (2, 1), (2, 2)




