class Solution {
public:

    // clever solution to use string as a key without needing custom hash function for unordered_map
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> m;

        for (int i = 0; i < strs.size(); i++) {
            std::array<int, 26> counts{};
            for (int j = 0; j < strs[i].size(); j++) {
                counts[strs[i][j] - 'a'] += 1;
            }

            std::string key = "";
            for (int k = 0; k < 26; k++) {
                key += std::to_string(counts[k]);
                key += "$";
            }

            m[key].push_back(strs[i]);
        }

        std::vector<std::vector<std::string>> ret;
        for (auto [key, value]: m) {
            ret.push_back(value);
        }

        return ret;
    }
};

// ["act","pots","tops","cat","stop","hat"]

// 
// 