class Solution {
public:
    int trap(vector<int>& height) {
        int leftMax = 0, rightMax = 0, l = 0, r = height.size() - 1;
        int total = 0;

        while (l < r) {
            if (height[l] < height[r]) {
                total += std::max(0, leftMax - height[l]);
                leftMax = std::max(leftMax, height[l]);
                l += 1;
            }
            else {
                total += std::max(0, rightMax - height[r]);
                rightMax = std::max(rightMax, height[r]);
                r -= 1;
            }
        }

        return total;
    }
};

// [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
// 