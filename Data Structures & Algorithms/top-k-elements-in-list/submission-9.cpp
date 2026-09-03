class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> counts{};

        for (auto &num : nums) {
            counts[num] += 1;
        }

        std::vector<std::vector<int>> buckets(nums.size() + 1);
        for (auto & [key, value] : counts) {
            buckets[value].push_back(key);
        }

        std::vector<int> ret{};
        for (int i = buckets.size() - 1; i >= 0; i--) {
            if (k == 0) {
                break;
            }

            while (buckets[i].size() > 0 && k > 0) {
                ret.push_back(buckets[i].back());
                buckets[i].pop_back();
                k--;
            }
        }

        return ret;
    }
};

// [1, 2, 2, 3, 3, 3], k = 2

// make counts
// 1 -> 1
// 2 -> 2
// 3 -> 3

// put in buckets
// buckets[1] = {1}

// buckets = [{1,}, {2}, {3}]