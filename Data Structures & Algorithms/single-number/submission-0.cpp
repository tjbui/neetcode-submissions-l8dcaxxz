class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            result = result ^ nums[i];
        }

        return result;
    }
};

// 7, 6, 6, 7, 8
// 0010 XOR 0010 = 0000
// all XOR will cancel out