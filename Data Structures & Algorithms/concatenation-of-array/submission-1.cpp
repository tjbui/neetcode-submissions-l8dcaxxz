class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        std::vector<int> concatArr = std::vector<int>(nums.size() * 2);

        for (int i = 0; i < nums.size(); i++) {
            concatArr[i] = nums[i];
            concatArr[i + nums.size()] = nums[i];
        }

        return concatArr;
    }
};

// 1, 4, 1, 2
// 