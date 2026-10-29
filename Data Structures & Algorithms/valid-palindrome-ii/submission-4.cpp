class Solution {
public:
    bool validPalindrome(string s) {
        int l = 0;
        int r = s.size() - 1;

        while (l < r) {
            if (s[l] != s[r]) {
                return isPalindrome(s.substr(l + 1, r - l)) ||
                       isPalindrome(s.substr(l, r - l));
            }

            l++;
            r--;
        }

        return true;
    }

private:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.size() - 1;

        while (l < r) {
            if (s[l] != s[r]) {
                return false;
            }
            l++;
            r--;
        }

        return true;
    }
};

// a b b b d a
// l         r

// a b b b d a
//   l     r

// a b d a
//   l r