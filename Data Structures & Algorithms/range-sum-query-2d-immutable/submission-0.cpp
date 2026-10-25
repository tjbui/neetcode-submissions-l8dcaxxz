class NumMatrix {
public:
    std::vector<std::vector<int>> prefSums{};

    NumMatrix(vector<vector<int>>& matrix) {
        prefSums = std::vector<std::vector<int>>(matrix.size() + 1);
  
        for (int i = 0; i <= matrix.size(); i++) {
            prefSums[i] = std::vector<int>(matrix[0].size() + 1, 0);
        }

        for (int i = 0; i < matrix.size(); i++) {
            int sum = 0;
            for (int j = 0; j < matrix[0].size(); j++) {
                sum += matrix[i][j];
                prefSums[i+1][j+1] =  sum + prefSums[i][j+1];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        int bottomRight = this->prefSums[row2 + 1][col2 + 1];

        int topLeft = this->prefSums[row1][col1];
        int upper = this->prefSums[row1][col2 + 1];
        int left = this->prefSums[row2 + 1][col1];

        return bottomRight - upper - left + topLeft;
    }
};

// 


/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */
