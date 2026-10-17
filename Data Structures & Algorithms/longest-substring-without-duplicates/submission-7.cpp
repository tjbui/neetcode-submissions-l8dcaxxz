class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::set<char> charSet{};

        int l = 0;
        int r = 0;
        int bestCount = 0;

        while (r < s.size()) {
            char nextChar = s[r];

            while (charSet.contains(nextChar)) {
                charSet.erase(s[l]);
                l++;
            }
            charSet.insert(nextChar);

            bestCount = std::max(bestCount, r - l + 1);
            r++;
        }

        return bestCount;
    }
};

// z x y z x y z
// l
// r

// z x y z x y z
// l
//   r

// z x y z x y z
// l
//     r

// z x y z x y z
// l
//       r