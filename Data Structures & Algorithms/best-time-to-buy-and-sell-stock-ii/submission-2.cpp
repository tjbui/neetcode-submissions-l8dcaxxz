class Solution {
public:
    int maxProfit(vector<int>& prices) { //greedy
        int profit = 0;

        for (int i = 1; i < prices.size(); i++) {
            profit += std::max(0, prices[i] - prices[i - 1]);
        }

        return profit;
    }
};

// [1, 15, 2, 40]

// anytime there is an upward price movement from i to i + 1, add the difference to profit