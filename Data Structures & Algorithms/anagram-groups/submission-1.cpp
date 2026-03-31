class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<std::string>> str_map;

        int i;
        for (i = 0; i < strs.size(); i++) {
            std::string curr_str = strs[i];
            std::sort(curr_str.begin(), curr_str.end());

            str_map[curr_str].push_back(strs[i]);
        }

        std::vector<std::vector<std::string>> result;
        for (const auto &pair: str_map) {
            result.push_back(pair.second);
        }
        return result;
    }
};

// act, cat
//
// sort(act) --> act
// sort(cat) --> act