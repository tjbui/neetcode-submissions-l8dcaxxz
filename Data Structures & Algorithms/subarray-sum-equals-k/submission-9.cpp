class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        std::unordered_map<int, int> prefCounts{};
        int totalSum = 0;
        int totalSubArr = 0;

        prefCounts[0] = 1;

        for (int i = 0; i < nums.size(); i++) {
            totalSum += nums[i];
            int needed = totalSum - k;
            totalSubArr += prefCounts[needed];
            prefCounts[totalSum]++;
        }

        return totalSubArr;
    }
};

