class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int p1 = 0;
        int p2 = 0;

        std::string mergedString{};
        while (p1 < word1.size() && p2 < word2.size()) {
            mergedString += word1[p1];
            mergedString += word2[p2];

            p1++;
            p2++;
        }

        while (p1 < word1.size()) {
            mergedString += word1[p1];

            p1++;
        }

        while (p2 < word2.size()) {
            mergedString += word2[p2];

            p2++;
        }

        return mergedString;
    }
};

//