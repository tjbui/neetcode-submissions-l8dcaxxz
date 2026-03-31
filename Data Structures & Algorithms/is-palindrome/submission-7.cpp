class Solution {
public:
    bool isPalindrome(string s) {
        std::string cleaned_str = "";

        for (int i = 0; i < s.length(); i++) {
            if (!std::isspace(s[i]) && std::isalnum(s[i])) {
                cleaned_str += std::tolower(s[i]);
            }
        }
        cout << cleaned_str;

        char *left = &cleaned_str[0];
        char *right = &cleaned_str[cleaned_str.length() - 1];

        while (left < right) {
            if (*left != *right) {
                return false;
            }
            left += 1;
            right -= 1;
        }

        return true;
    }
};
