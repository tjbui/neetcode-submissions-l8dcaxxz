class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums;
        }

        std::vector<int> left(nums.begin(), nums.begin() + (nums.size() / 2));
        std::vector<int> right(nums.begin() + (nums.size() / 2), nums.begin() + nums.size());

        std::vector<int> left_sorted = sortArray(left);
        std::vector<int> right_sorted = sortArray(right);

        return merge(left_sorted, right_sorted);
    }

    std::vector<int> merge(std::vector<int> &v1, std::vector<int> &v2) {
        std::vector<int> merged{};

        int p1 = 0;
        int p2 = 0;

        while (p1 < v1.size() && p2 < v2.size()) {
            if (v1[p1] < v2[p2]) {
                merged.push_back(v1[p1]);
                p1 += 1;
            }
            else {
                merged.push_back(v2[p2]);
                p2 += 1;
            }
        }

        while (p1 < v1.size()) {
            merged.push_back(v1[p1]);
            p1 += 1;
        }

        while (p2 < v2.size()) {
            merged.push_back(v2[p2]);
            p2 += 1;
        }

        return merged;
    }
};

// [10, 9, 1, 1, 1, 2, 3, 1]
//   0  1  2  3  4  5  6  7

// [10, 9, 1, 1] [1, 2, 3, 1]

// [10, 9] [1, 1] [1, 2] [3, 1]

// [10] [9] [1] [1] [1] [2] [3] [1]

// 