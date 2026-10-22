class Solution {
public:
    static constexpr int size = 3;

    void sortColors(vector<int>& nums) {
        std::array<int, size> counts{};

        for (auto &num : nums) {
            counts[num]++;
        }

        int ind = 0;
        for (int i = 0; i < size; i++) {
            while (counts[i] > 0) {
                nums[ind] = i;
                ind++;
                counts[i]--;
            }
        }
    }
};

// [ 1, 0, 1, 2 ]

// {0 -> 1, 1 -> 2, 2 -> 1}

// i = 0
// counts[i] = 1
// ind = 0
// [ 0, 1, 1, 2 ]



