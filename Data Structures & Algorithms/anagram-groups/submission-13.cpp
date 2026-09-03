class Solution {
public:
    struct ArrayHash {
        std::size_t operator()(const std::array<int, 26> &arr) const {
            std::string_view arr_to_str(reinterpret_cast<const char *>(arr.data()),   
                                        arr.size() * 26);

            return std::hash<std::string_view>{}(arr_to_str);
        }
    };

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::array<int, 26>, std::vector<string>, ArrayHash> m{};

        for (auto &curr_str : strs) {
            std::array<int, 26> char_counts{};

            for (auto &curr_char : curr_str) {
                char_counts[curr_char - 'a'] += 1;
            }

            m[char_counts].push_back(curr_str);
        }

        std::vector<std::vector<std::string>> ret{};
        for (auto [key, value] : m) {
            ret.push_back(value);
        }

        return ret;
    }
};

// ["act","pots","tops","cat","stop","hat"]
//
// "act"
// [1, 0, 1, 0, 0, ...] --> ["act"]
