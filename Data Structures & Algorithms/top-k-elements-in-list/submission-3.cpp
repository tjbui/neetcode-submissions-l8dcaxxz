class Solution {
public:
    /* O(n) Bucket sort */

    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> cmap;

        for (int i : nums) {
            cmap[i] += 1;
        }

        std::vector<std::vector<int>> count_vec(nums.size() + 1);
        for (auto p : cmap) {
            count_vec[p.second].push_back(p.first);
        }

        std::vector<int> ret;
        int counter = 0;
        for (int i = count_vec.size() - 1; i >= 0; i--) {
            if (counter >= k) {
                break;
            }
            
            if (!count_vec[i].empty()) {
                while ((counter < k) && (!count_vec[i].empty())) {
                    ret.push_back(count_vec[i].back());
                    count_vec[i].pop_back();
                    counter++;
                }
            }
        }

        return ret;
    }
};

// 1 --> 1
// 2 --> 2
// 3 --> 3
// [0, 0, 0, 0, 0, 0]
// [0, 0, 0, 0, 0, 0]

// [[], [1, 2], []]
// 
