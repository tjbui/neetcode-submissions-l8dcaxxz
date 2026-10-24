class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        std::unordered_map<int, int> counts{};

        int majCount = nums.size() / 3 + 1;
        std::vector<int> majElements{};
        for (auto &num : nums) {
            counts[num]++;

            if (counts[num] == majCount) {
                majElements.push_back(num);
            }
        }

        return majElements;
    }
};

// 5, 2, 3, 2, 2, 2, 2, 5, 5, 5

// 