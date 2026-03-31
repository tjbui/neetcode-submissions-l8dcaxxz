class Solution {
public:
    bool isValid(string s) {
        std::stack<char> p_stack;

        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                p_stack.push(s[i]);
            }
            else if (s[i] == ')' || s[i] == '}' || s[i] == ']') {
                if (p_stack.empty()) {
                    return false;
                }

                char popped_char = p_stack.top();

                if (!check_parenthesis(popped_char, s[i])) {
                    return false;
                }
                p_stack.pop();
            }
            else {
                return false;
            }
        }

        if (p_stack.size() != 0) {
            return false;
        }
        return true;
    }

    bool check_parenthesis(char popped, char curr) {
        if (popped == '{' && curr == '}') {
            return true;
        }
        if (popped == '(' && curr == ')') {
            return true;
        }
        if (popped == '[' && curr == ']') {
            return true;
        }

        return false;
    }
};

// ( ( {))
// top    {
//        (
// bottom (
