class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1;

        while (left <= right) {
            int middle = (right + left) / 2;

            if (nums[middle] == target) {
                return middle;
            }
            else if (nums[middle] > target) {
                right = middle - 1;
            }
            else {
                left = middle + 1;
            }
        }

        return -1;
    }
};

// nums = [-1, 0, 2, 4, 6, 8], target = 4
//          0  1  2  3  4  5
//          l              r



// nums =  [1, 2, 3, 4, 5, 6, 7], target = 2
//          l        m        r 

// nums =  [1, 2, 3, 4, 5, 6, 7], target = 2
//          l  m  r             


