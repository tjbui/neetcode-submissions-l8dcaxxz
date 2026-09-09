class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> nums_set{};

        for (auto &num : nums) {
            nums_set.insert(num);
        }

        int max_length = 0;
        while (nums_set.size() > 0) {
            int num = *nums_set.begin();

            while (nums_set.contains(num - 1)) {
                num -= 1;
            }

            int length = 1;
            nums_set.erase(num);
            while (nums_set.contains(num + 1)) {
                num += 1;
                length += 1;
                nums_set.erase(num - 1);
            }

            max_length = std::max(length, max_length);
        }

        return max_length;
    }
};

// [2, 20, 4, 10, 3, 4, 5]

// o(nlogn) solution:
// [2, 3, 4, 4, 5, 10, 20]

// O(n):
// [3, 20, 4, 10, 2, 4, 5]

// set: [2, 20, 4, 10, 3, 4, 5]

// i = 3
// (3 - 1) in set --> yes, continue

// i = 2
// (2 - 1) in set --> no, initialize length = 1

// i = 2, length = 1
// (2 + 1) in set --> yes, length++

// i = 3, length = 2
// (3 + 1) in set --> yes, length++

// ...