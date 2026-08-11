class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // using std::array and std::map for O(logn) insertion instead
        std::map<std::array<int, 26>, std::vector<std::string>> m{};

        for (const auto &str: strs) {
            std::array<int, 26> counts{};
            for (const auto &c: str) {
                counts[c - 'a'] += 1;
            }

            m[counts].push_back(str);
        }

        std::vector<std::vector<std::string>> ret{};
        for (auto [key, value]: m) {
            ret.push_back(value);
        }

        return ret;
    }
};

// ["act","pots","tops","cat","stop","hat"]

// map (1, 0, 1, 0, 0, ...) -> ["act", "cat", ]
//