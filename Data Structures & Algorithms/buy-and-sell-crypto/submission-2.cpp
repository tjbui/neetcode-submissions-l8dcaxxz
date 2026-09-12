class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int r = 1;
        int max = 0;

        while (r < prices.size()) {
            max = std::max(max, prices[r] - prices[l]);

            if (prices[r] < prices[l]) l = r;
            r++;
        }

        return max;
    }
};


// we want the buy day to be the minimum to the left of the sell day

// [10, 1, 5, 6, 7, 1]
//   b              
//      s
// max = 0

// [10, 3, 5, 1, 6, 7, 1]
//      b              
//         s
// max = 2

// [10, 3, 5, 1, 6, 7, 1]
//      b                 
//            s
// max = 2

// [10, 3, 5, 1, 6, 7, 1]
//            b                  
//               s
// max = 2