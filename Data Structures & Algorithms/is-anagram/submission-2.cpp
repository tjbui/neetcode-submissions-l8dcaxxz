class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> s_map;
        std::unordered_map<char, int> t_map;

        for (char &c : s) {
            s_map[c] += 1;
        }
        for (char &c : t) {
            t_map[c] += 1;
        }

        return s_map == t_map;
    }
};

// "racecar"
// r --> 2
// a --> 2
// c --> 2
// e --> 1