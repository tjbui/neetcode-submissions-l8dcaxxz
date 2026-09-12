class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int max = 0;
        int l = 0;
        int r = 0;
        std::unordered_set<char> seen{};

        while (r < s.size()) {
            while (seen.contains(s[r])) {
                seen.erase(s[l]);
                l += 1;
            }
            
            max = std::max(max, r - l + 1);
            seen.insert(s[r]);
            r++;
        }

        return max;
    }
};

// "zxyzxyz"
// 
// "z x y z x y z"
//  l
//  r

// "z x y z x y z"
//  l
//    r

// "z x y z x y z"
//  l
//      r

// "z x y z x y z"
//  l
//        r




