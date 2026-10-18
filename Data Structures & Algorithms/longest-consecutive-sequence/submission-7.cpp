class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> numsSet = std::unordered_set(nums.begin(), nums.end());
        
        int best = 0;
        while (!numsSet.empty()) {
            int currNum = *numsSet.begin();

            while (numsSet.contains(currNum - 1)) {
                currNum--;
            }

            numsSet.erase(currNum);
            int currConsecSeq = 1;
            while (numsSet.contains(currNum + 1)) {
                numsSet.erase(currNum);
                currConsecSeq++;
                currNum++;
            }

            best = std::max(best, currConsecSeq);
        }

        return best;
    }
};

// [2, 30, 4, 10, 3, 4, 5]

// [10, 9, 8, 7, 6, 5, 4, 3]

// go to bottom (3)
// go back up and erase while processing