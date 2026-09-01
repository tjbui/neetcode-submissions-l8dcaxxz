class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> s{};

        for (int &i: nums) {
            if (s.contains(i)) {
                return true;
            }

            s.insert(i);
        }

        return false;
    }
};