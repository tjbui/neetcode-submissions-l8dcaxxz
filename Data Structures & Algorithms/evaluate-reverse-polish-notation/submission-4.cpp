class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::stack<int> st;
        
        for (const std::string& token : tokens) {
            if (token == "+" || token == "-" || token == "*" || token == "/") {
                int right = st.top(); 
                st.pop();

                int left = st.top(); 
                st.pop();
                
                if (token == "+") st.push(left + right);
                else if (token == "-") st.push(left - right);
                else if (token == "*") st.push(left * right);
                else if (token == "/") st.push(left / right);
            } else {
                st.push(std::stoi(token));
            }
        }
        return st.top();
    }
};

// ["1","2","+","3","*","4","-"]


// +
// 2
// 1

// *
// 3
// 3

// -
// 4
// 9