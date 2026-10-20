class Solution {
public:
    int majorityElement(vector<int>& nums) {
        std::unordered_map<int, int> counts{};

        int maxCount = 0;
        int maxElement = 0;
        for (auto& num : nums) {
            counts[num]++;

            if (counts[num] > maxCount) {
                maxElement = num;
                maxCount = counts[num];
            }
        }

        return maxElement;
    }
};