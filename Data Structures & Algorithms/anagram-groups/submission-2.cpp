class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, std::vector<string>> m;

        int i;
        for (i = 0; i < strs.size(); i++) {
            std::string unsorted = strs[i];

            std::sort(strs[i].begin(), strs[i].end());
            m[strs[i]].push_back(unsorted);
        }

        std::vector<std::vector<std::string>> result;

        for (const auto& p : m) {
            result.push_back(p.second);
        }
        return result;

    }
};
