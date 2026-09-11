class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size() - 1;

        int max = 0;
        while (l < r) {
            int area = (r - l) * std::min(heights[l], heights[r]);

            max = std::max(max, area);
            if (heights[l] < heights[r]) l += 1;
            else r -= 1;
        }

        return max;
    }
};

// [1, 7, 2, 5, 4, 7, 3, 6]
// 
// bottleneck is the shorter one
// we can move the taller one because the pointer at the shorter one is CAPPED at exactly that.
// no matter how much taller another one is it will have the same height since its shorter and
// with a smaller width

// [1, 7, 2, 5, 4, 7, 3, 6]

// 
//
// 