class Solution {
public:

    // use std::array as key to std::unordered_map. unordered_map needs
    // a hash function, so we need to define a custom one
    struct ArrayHash {
        std::size_t operator()(const std::array<int, 26> &arr) const {
            std::string_view arr_to_str(reinterpret_cast<const char *>(arr.data()),
                                        arr.size() * 26);

            return std::hash<std::string_view>{}(arr_to_str);
        }
    };

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::array<int, 26>, std::vector<string>, ArrayHash>
                                                map_arr_to_vec{};
        
        for (auto &curr_string : strs) {
            std::array<int, 26> chars_arr{};

            for (auto &curr_char : curr_string) {
                chars_arr[curr_char - 'a'] += 1;
            }

            map_arr_to_vec[chars_arr].push_back(curr_string);
        }

        std::vector<std::vector<std::string>> ret{};
        for (auto [key, value] : map_arr_to_vec) {
            ret.push_back(value);
        }

        return ret;
    }
};

// strs = ["act","pots","tops","cat","stop","hat"]
// 
// "act"
// [1, 0, 1, ...]