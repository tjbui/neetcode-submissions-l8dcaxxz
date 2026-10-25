class NumArray {
public:
    std::vector<int> prefSums{};

    NumArray(vector<int>& nums) {
        prefSums = std::vector<int>(nums.size());

        int sum = 0;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            this->prefSums[i] = sum;
        }
    }
    
    int sumRange(int left, int right) {
        if (left == 0) {
            return prefSums[right];
        }

        return prefSums[right] - prefSums[left - 1];
    }
};

// [-2,0,3,-5,2,-1]

// [0, 2] --> 1

// 

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */
