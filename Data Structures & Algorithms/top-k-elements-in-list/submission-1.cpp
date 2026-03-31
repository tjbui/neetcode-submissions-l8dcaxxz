class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> count_map;

        for (int i = 0; i < nums.size(); i++) {
            count_map[nums[i]]++;
        }


        std::vector<std::pair<int, int>> vec;
        for (auto & p : count_map) {
            vec.push_back(p);
        }

        std::sort(vec.begin(), vec.end(), [](auto &a, auto &b){
            return a.second > b.second;
        });

        vector<int> result;
        for (int i = 0; i < k; i++) {
            result.push_back(vec[i].first);
        }

        return result;
    }
};

// 1 2 2 3 3 3, k = 2 --> 3 is most freq, 2 is 2nd most freq
// 1 4 4 4 3 3 3 --> invalid input since not unique
//