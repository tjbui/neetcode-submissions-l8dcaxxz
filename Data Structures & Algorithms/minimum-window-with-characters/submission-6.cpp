class Solution {
public:
string minWindow(string s, string t) {
        int l = 0;
        int bestStart = 0, bestLen = INT_MAX;

        std::unordered_map<char, int> window;
        std::unordered_map<char, int> need;
        for (char c : t) need[c]++;

        for (int r = 0; r < s.size(); r++) {
            window[s[r]] += 1;

            while (checkWindow(need, window)) {
                if (r - l + 1 < bestLen) {
                    bestLen = r - l + 1;
                    bestStart = l;
                }
                window[s[l]] -= 1;
                l += 1;
            }
        }

        return bestLen == INT_MAX ? "" : s.substr(bestStart, bestLen);
    }

    bool checkWindow(std::unordered_map<char, int> &need,
                     std::unordered_map<char, int> &window) {
        for (auto &[c, cnt] : need) {
            auto it = window.find(c);
            if (it == window.end() || it->second < cnt) {
                return false;
            }
        }
        return true;
    }
};

// "OUZODYXAZV", t = "XYZ"
// 

// counts = {O -> 1}
// "O U Z O D Y X A Z V", t = "X Y Z"
//  l
//  r

// counts = {O -> 1, U -> 1}
// "O U Z O D Y X A Z V", t = "X Y Z"
//  l
//    r

// counts = {O -> 1, U -> 1, Z -> 1, ...}
// "O U Z O D Y X A Z V", t = "X Y Z"
//  l
//              r
// now valid, lets shrink

// counts = {O -> 1, U -> 1, Z -> 1, ...}
// "O U Z O D Y X A Z V", t = "X Y Z"
//      l
//              r
// shrinking more would make invalid so stop shrinking