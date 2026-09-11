class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size() - 1;

        while (l < r) {
            int sum = numbers[l] + numbers[r];

            if (sum < target) {
                l += 1;
            }
            else if (sum > target) {
                r -= 1;
            }
            else {
                return std::vector<int>{l + 1, r + 1};
            }
        }

        return std::vector<int>{};
    }
};

// [1, 2, 3, 4]
// 