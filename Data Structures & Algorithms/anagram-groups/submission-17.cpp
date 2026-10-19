class Solution {
public:
    struct ArrayHash {
        std::size_t operator()(const std::array<int, 26> &arr) const {
            std::string_view strView(reinterpret_cast<const char *>(arr.data()), arr.size() * sizeof(int));

            return std::hash<std::string_view>{}(strView);
        }
    };

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::array<int, 26>, std::vector<std::string>, ArrayHash> countsToList{};

        for (auto &currStr : strs) {
            std::array<int, 26> charCounts{};
            for (auto &currChar : currStr) {
                charCounts[currChar - 'a'] += 1;
            }

            countsToList[charCounts].push_back(currStr);
        }

        std::vector<std::vector<std::string>> anagramsVec{};
        for (auto &[key, value] : countsToList) {
            anagramsVec.push_back(std::move(value));
        }

        return anagramsVec;
    }
};

// ["act", "pots", "tops", "cat", "stop", "hat"]

// [a -> 1, b, -> 0, c -> 1, ..., t -> 1, ...] -> ["act", "cat"]

// map std::array<int, 26> to std::vector<std::string>>

// 