class Solution {
public:

    // use std::array as a key with std::map - no hash function needed bceause std::map uses RB tree
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::map<std::array<int, 26>, std::vector<std::string>> m{};

        for (auto &s : strs) {
            std::array<int, 26> a{};
            for (auto &c : s) {
                
                // strs is all lowercase
                a[c - 'a'] += 1;
            }

            m[a].push_back(s);
        }

        std::vector<std::vector<string>> ret{};
        for (auto [key, value] : m) {
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