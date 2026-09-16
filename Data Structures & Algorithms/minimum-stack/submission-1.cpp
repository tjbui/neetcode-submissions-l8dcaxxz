class MinStack {
public:
    std::stack<int> st{};
    std::stack<int> minSt{};

    MinStack() = default;
    
    void push(int val) {
        st.push(val);

        if (minSt.empty()) {
            minSt.push(val);
        }
        else {
            minSt.push(std::min(val, minSt.top()));
        }
    }
    
    void pop() {
        st.pop();
        minSt.pop();
    }
    
    int top() {
        return st.top();
    }
    
    int getMin() {
        return minSt.top();
    }
};

          
// 1      // 1

// 2      // 1
// 1      // 1

// 0      // 0
// 2      // 1
// 1      // 1