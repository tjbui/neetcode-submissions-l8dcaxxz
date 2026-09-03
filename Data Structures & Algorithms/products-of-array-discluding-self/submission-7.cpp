class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        std::vector<int> left_prod(nums.size());
        int total = nums[0];
        left_prod[0] = 1;
        for (int i = 1; i < nums.size(); i++) {
            left_prod[i] = total;
            total *= nums[i];
        }
        
        std::vector<int> right_prod(nums.size());
        total = nums[nums.size() - 1];
        right_prod[nums.size() - 1] = 1;
        for (int i = nums.size() - 2; i >= 0; i--) {
            right_prod[i] = total;
            total *= nums[i];
        }

        std::vector<int> ret{};
        for (int i = 0; i < nums.size(); i++) {
            ret.push_back(left_prod[i] * right_prod[i]);
        }

        return ret;
    }
};

// [1, 2, 4, 6]
// [48, 24, 12, 8]

// [2 * 4 * 6, 1 * 4 * 6, 1 * 2 * 6]

// [1, 2, 4, 6]
// left_prod =  [1, 1, 2, 8]
// right_prod = [48, 24, 6, 1]

// [1, 2, 0, 2, 2, 0]
// 

// [1, 2, 3, 0, 2, 1]
// [0, 0, 0, 12, 0, 0]