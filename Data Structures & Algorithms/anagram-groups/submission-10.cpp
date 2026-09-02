class Solution {
public:

    // clever solution to use string as a key without needing custom hash function for unordered_map
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> map_arr_to_vec{};

        for (auto &curr_string : strs) {
            std::array<int, 26> counts{};

            for (auto &curr_char : curr_string) {
                counts[curr_char - 'a'] += 1; // strs is all lowercase
            }

            std::string str_key = "";
            for (auto &curr_int : counts) {
                str_key += std::to_string(curr_int);
                str_key += "$";
            }

            map_arr_to_vec[str_key].push_back(curr_string);
        }

        std::vector<std::vector<std::string>> ret;
        for (auto [key, value]: map_arr_to_vec) {
            ret.push_back(value);
        }

        return ret;
    }
};

// ["act","pots","tops","cat","stop","hat"]

// 
// 