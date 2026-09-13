class Solution {
public:
    bool isValid(string s) {
        std::stack<char> st{};

        for (auto &curr_char : s) {
            if (curr_char == '}') {
                if (!st.empty() && st.top() == '{') st.pop();
                else return false;
            }
            else if (curr_char == ')') {
                if (!st.empty() && st.top() == '(') st.pop();
                else return false;
            }
            else if (curr_char == ']') {
                if (!st.empty() && st.top() == '[') st.pop();
                else return false;
            }
            else {
                st.push(curr_char);
            }
        }

        return st.empty();
    }
};


