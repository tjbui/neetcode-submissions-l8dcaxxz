class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> m;

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            
            if (m.contains(diff)) {
                return {m[diff], i};
            }

            m[nums[i]] = i;
        }

        return {};
    }
};

// 2, 5, 3, 10
// 