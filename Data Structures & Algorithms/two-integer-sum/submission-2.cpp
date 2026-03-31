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

        return {0, 0};
    }
};


// [3, 4, 5, 6] target = 7
// 3: needs 4. Not in map. 3 --> 0
// 4: needs 3. m[3] = 0
// return