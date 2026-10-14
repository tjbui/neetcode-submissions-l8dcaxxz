class Solution {
public:
    int findMin(vector<int> &nums) {
        int l = 0;
        int r = nums.size() - 1;

        while (l < r) {
            int m = (l + r) / 2;

            if (nums[m] > nums[r]) {
                l = m + 1;
            }
            else {
                r = m;
            }
        }

        return nums[l];
    }
};

// [3, 4, 5, 1, 2]
//  l           r
//        m
// r < m so its on right of m

// [4, 5, 1, 2, 3]
//  l           r
//        m
// r > m so its on left of m inclusive

// [1, 2]
//  l  r
//  m


// [1, 2, 3, 4, 5]

// [2, 3, 4, 5, 1]

// [5, 1, 2, 3, 4]