class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int curr = 0;
        int repl = 0;

        while (curr < nums.size()) {
            if (nums[curr] == val) {
                curr++;
                continue;
            }

            nums[repl] = nums[curr];
            repl++;
            curr++;
        }

        return repl;
    }
};

// [3, 2, 3, 3, 5, 4, 3], val = 3
 
//    3,    2,    3,    3,    5,    4,    3
//    curr
//    repl

//    3,    2,    3,    3,    5,    4,    3
//          curr
//    repl

//    2,    2,    3,    3,    5,    4,    3
//                curr
//          repl

//    2,    2,    3,    3,    5,    4,    3
//                      curr
//          repl

//    2,    2,    3,    3,    5,    4,    3
//                            curr
//          repl

//    2,    5,    3,    3,    5,    4,    3
//                                  curr
//                repl

//    2,    5,    4,    3,    5,    4,    3
//                                        curr
//                      repl