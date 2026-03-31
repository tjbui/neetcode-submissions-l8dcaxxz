class Solution {
public:
    int missingNumber(vector<int>& nums) {
        std::unordered_set<int> s;
        for (int i: nums) {
            s.insert(i);
        }

        for (int i = 0; i <= nums.size(); i++) {
            if (!s.contains(i)) {
                return i;
            }
        }

        return -1;
    }
};

// 0000 0001
// 