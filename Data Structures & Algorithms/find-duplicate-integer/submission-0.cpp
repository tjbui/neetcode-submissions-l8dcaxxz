class Solution {
public:
    int findDuplicate(vector<int>& nums) { // negative thing
        for (auto num : nums) {
            num = std::abs(num);

            if (nums[num] < 0) {
                return num;
            }

            nums[num] *= -1;
        }

        return -1;
    }
};

// [1, 2, 3, 2, 2], n = 4

// [1, 2, 3, 2, 2]
//  i
// is arr[1] negative? no

// [1, -2, 3, 2, 2]
//      i
// is arr[2] negative? no

// [1, -2, -3, 2, 2]
//          i
// is arr[3] negative? no

// [1, -2, -3, -2, 2]
// is arr[2] negative? yes
// 2 is the duplicate

