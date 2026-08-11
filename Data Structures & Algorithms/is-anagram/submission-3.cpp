class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<int, int> s_count;
        std::unordered_map<int, int> t_count;

        for (int i = 0; i < s.size(); i++) {
            s_count[s[i]] += 1;
        }
        
        for (int i = 0; i < t.size(); i++) {
            t_count[t[i]] += 1;
        }

        if (s_count == t_count) {
            return true;
        }

        return false;
    }
};
