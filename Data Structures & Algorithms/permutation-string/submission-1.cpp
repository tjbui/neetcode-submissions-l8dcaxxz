class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        std::unordered_map<char, int> s1Counts{};
        for (auto &c : s1) {
            s1Counts[c] += 1;
        }

        int l = 0;
        int r = 0;
        std::unordered_map<char, int> s2Counts{};
        while (r < s2.size()) {
            s2Counts[s2[r]] += 1;

            if (s1Counts == s2Counts) {
                return true;
            }

            if (r - l + 1 == s1.size()) {
                s2Counts[s2[l]] -= 1;
                if (s2Counts[s2[l]] == 0) {
                    s2Counts.erase(s2[l]);
                }
                l++;
            }
            r++;
        }

        return false;
    }
};

// s1 = "abc", s2 = "lecabee"
//
// s1Counts = {a -> 1, b -> 1, c -> 1}

// s2Counts = {l -> 1}
// "l e c a b e e"
//  l
//  r

// s2Counts = {l -> 1, e -> 1}
// "l e c a b e e"
//  l
//    r