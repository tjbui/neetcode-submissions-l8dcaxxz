class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0) {
            return "";
        }

        int prefCount = 0;
        for (int i = 0; i < strs[0].size(); i++) {
            char currChar = strs[0][i];

            for (int j = 1; j < strs.size(); j++) {
                if (i > strs[j].size() || currChar != strs[j][i]) {
                    return strs[0].substr(0, prefCount);
                }
            }

            prefCount++;
        }

        return strs[0].substr(0, prefCount);
    }
};

// ["bat","bag","bank","band"]
// ba

// "bat", "bag" "bank", "band"
//  c      c     c       c