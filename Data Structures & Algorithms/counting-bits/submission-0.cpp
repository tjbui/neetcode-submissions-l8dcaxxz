class Solution {
public:
    vector<int> countBits(int n) {
        std::vector<int> v;
        int count;

        for (int curr = 0; curr <= n; curr++) {
            count = 0;

            for (int i = 0; i < 32; i++) {
                if (curr & (1 << i)) {
                    count += 1;
                }
            }

            v.push_back(count);
        }

        return v;
    }
};

// 4 --> 100
// 5 --> 101
// 6 --> 110
// 7 --> 111