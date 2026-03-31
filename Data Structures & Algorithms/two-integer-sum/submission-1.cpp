class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> m;

        for (int i = 0; i < nums.size(); i++) {

            int needed = target - nums[i];

            if (m.contains(needed)) {
                return {m[needed], i};
            }

            m[nums[i]] = i;
        }

        return {};
    }
};
