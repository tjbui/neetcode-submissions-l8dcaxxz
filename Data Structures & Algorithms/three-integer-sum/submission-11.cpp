class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());

        std::set<array<int, 3>> seen{};
        vector<vector<int>> result{};
        for (int curr_idx = 0; curr_idx < nums.size(); curr_idx++) {
            int l = curr_idx + 1;
            int r = nums.size() - 1;

            while (l < r) {
                if (nums[l] + nums[r] < -nums[curr_idx]) {
                    l += 1;
                }
                else if (nums[l] + nums[r] > -nums[curr_idx]) {
                    r -= 1;
                }
                else {
                    if (!seen.contains(std::array<int, 3>{nums[curr_idx], nums[l], nums[r]})) {
                        result.push_back(std::vector<int>{nums[curr_idx], nums[l], nums[r]});
                        seen.insert(std::array<int, 3>{nums[curr_idx], nums[l], nums[r]});
                    }
                    while (l < r && nums[l] == nums[l + 1]) l++;
                    while (l < r && nums[r] == nums[r - 1]) r--;
                    l++;
                    r--;
                }
            }
        }

        return result;
    }
};


// curr = -4
// [-4, -1, -1, 1, 3, 5, 5]
//       l               r

// [[-4, -1, 5], [-4, 3, 1]]



