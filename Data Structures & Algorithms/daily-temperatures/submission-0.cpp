class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::unordered_map<int, int> index_to_days{};
        std::stack<std::array<int, 2>> st{};
        
        for (int i = 0; i < temperatures.size(); i++) {
            int temp = temperatures[i];

            if (!st.empty()) {
                while (!st.empty() && st.top()[0] < temp) {
                    index_to_days[st.top()[1]] = i - st.top()[1];
                    st.pop();
                }
            }

            st.push(std::array<int, 2>{temp, i});
        }

        std::vector<int> ret{};
        for (int i = 0; i < temperatures.size(); i++) {
            ret.push_back(index_to_days[i]);
        }

        return ret;
    }
};


// [30, 38, 30, 36, 35, 40, 28]
// [1, 4, 1, 2, 1, 0, 0]

// Process 30 
// (30, 0)

// Process 38, 38 is greater than 30. Pop and add 1, then push 38
// (38, 1)

// Process 30
// (30, 2)
// (38, 1)

// Process 36, 36 is greater than 30. Pop and 1 to 30s, then push 36
// 36
// 38

// Process 35
