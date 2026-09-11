class Solution {
public:
    bool isPalindrome(string s) {
        std::string cleaned_string{};

        for (auto &c: s) {
            if (std::isalnum(c)) {
                cleaned_string += std::tolower(c);
            }
        }

        int l = 0;
        int r = cleaned_string.size() - 1;

        while (r > l) {
            if (cleaned_string[l] != cleaned_string[r]) {
                return false;
            }
            l += 1;
            r -= 1;
        }

        return true;
    }
};

// "Was it a car or a cat I saw?"
//  l                         r