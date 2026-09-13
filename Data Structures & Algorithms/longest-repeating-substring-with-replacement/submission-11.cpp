class Solution {
public:
    int characterReplacement(string s, int k) {
        std::unordered_map<char, int> counts{};
        int l = 0;
        int r = 0;
        int maxLength = 0;

        while (r < s.size()) {
            counts[s[r]] += 1;

            int maxCounts = 0;
            for (auto &[key, value] : counts) {
                maxCounts = std::max(maxCounts, value);
            }

            int length = r - l + 1;
            while (length - maxCounts > k) {
                counts[s[l]] -= 1;
                l++;

                maxCounts = 0;
                for (auto &[key, value] : counts) {
                    maxCounts = std::max(maxCounts, value);
                }
                
                length = r - l + 1;
            }

            maxLength = max(maxLength, length);
            r++;
        }

        return maxLength;
    }
};

// "AAABABB", k = 1
//
// counts = {A -> 1}
// "A A A B A B B"
//  l
//  r

// check if: length - maxCounts > k
// this means invalid window

// counts = {A -> 2}
// "A A A B A B B"
//  l
//    r

// counts = {A -> 2}
// "A A A B A B B"
//  l
//      r