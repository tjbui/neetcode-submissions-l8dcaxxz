class Solution {
public:

    // use std::array as a key with std::map - no hash function needed 
    // bceause std::map uses RB tree. O(nlogn)
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::map<std::array<int, 26>, std::vector<std::string>> map_arr_to_vec{};

        for (auto &s : strs) {
            std::array<int, 26> a{};
            for (auto &c : s) {
                a[c - 'a'] += 1; // strs is all lowercase
            }

            map_arr_to_vec[a].push_back(s);
        }

        std::vector<std::vector<string>> ret{};
        for (auto [key, value] : map_arr_to_vec) {
            ret.push_back(value);
        }

        return ret;
    }
};

// strs = ["act","pots","tops","cat","stop","hat"]

// "act"
// a -> 1, c -> 1, t -> 1, 
// [1, 1, 1, 0, 0, ...]
// 