class Solution {
public:
    /* attempt 2 clean */

    bool isValid(string s) {
        std::stack<char> st;

        for (char c: s) {
            if (c == '{' || c == '[' || c == '(') {
                st.push(c);
            }
            else {
                if (st.empty()) {
                    return false;
                }

                if ((st.top() == '(' && c != ')') ||
                    (st.top() == '{' && c != '}') ||
                    (st.top() == '[' && c != ']')
                    ) {
                    return false;
                }
                st.pop();
            }
        }

        if (st.empty()) {
            return true;
        }
        return false;
    }
};
