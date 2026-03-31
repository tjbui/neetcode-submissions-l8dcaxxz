class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        std::unordered_map<char, int> freqs;
        std::unordered_map<char, int> freqt;

        for (int i = 0; i < s.length(); i++) {
            freqs[s[i]]++;
        }
        for (int i = 0; i < t.length(); i++) {
            freqt[t[i]]++;
        }

        return freqs == freqt;
        
    }
};
