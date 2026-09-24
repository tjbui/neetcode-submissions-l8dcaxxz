class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int right = *std::max_element(piles.begin(), piles.end());
        int left = 1;

        while (left < right) {
            int middle = (right + left) / 2;

            int hours = 0;
            for (auto &bananas : piles) {
                hours += std::ceil( (double) bananas / middle );
            }

            if (hours <= h) {
                right = middle;
            }
            else if (hours > h) {
                left = middle + 1;
            }
        }

        return left;
    }
};

// [25, 10, 23, 4], h = 4
// 
// max(piles) = 25
// 

// [25] if rate is 6, it will be 5. so ceil(25 / 6) = 5