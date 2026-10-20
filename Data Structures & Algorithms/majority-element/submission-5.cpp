class Solution {
public:
    int majorityElement(vector<int>& nums) {
        if (nums.empty()) {
            return -1;
        }

        int curr = nums[0];
        int count = 0;
        for (auto &num : nums) {
            if (curr != num) {
                if (count == 0) curr = num;
                else count--;
            }
            else {
                count++;
            }
        }

        return curr;
    }
};

// [5, 5, 1, 1, 1, 5, 5]

// [5, 5, 1, 1, 1, 5, 5]
//  i
// curr = 5
// count = 1

// [5, 5, 1, 1, 1, 5, 5]
//     i
// curr = 5
// count = 2

// [5, 5, 1, 1, 1, 5, 5]
//        i
// curr = 5
// count = 1

// [5, 5, 1, 1, 1, 5, 5]
//           i
// curr = 1
// count = 0

// [5, 5, 1, 1, 1, 5, 5]
//              i
// curr = 1
// count = 1

// [5, 5, 1, 1, 1, 5, 5]
//                 i
// curr = 5
// count = 0

// [5, 5, 1, 1, 1, 5, 5]
//                    i
// curr = 5
// count = 1