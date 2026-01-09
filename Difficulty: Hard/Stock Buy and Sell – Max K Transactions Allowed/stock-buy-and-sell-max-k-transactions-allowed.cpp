class Solution {
  public:
    int maxProfit(vector<int>& prices, int k) {
        int n = prices.size();
        
        if (n == 0 || k == 0) return 0;
        
        // If k large enough → unlimited transactions
        if (2 * k >= n) {
            int profit = 0;
            for (int i = 1; i < n; i++) {
                if (prices[i] > prices[i - 1]) {
                    profit += prices[i] - prices[i - 1];
                }
            }
            return profit;
        }
        
        // dp[t][0] = max profit with t transactions, NOT holding
        // dp[t][1] = max profit with t transactions, HOLDING  
        vector<vector<int>> dp(k + 1, vector<int>(2, 0));
        for (int t = 1; t <= k; t++) {
            dp[t][1] = INT_MIN;
        }
        
        for (int i = 0; i < n; i++) {
            for (int t = k; t >= 1; t--) {
                // Sell
                dp[t][0] = max(dp[t][0], dp[t][1] + prices[i]);
                // Buy  
                dp[t][1] = max(dp[t][1], dp[t - 1][0] - prices[i]);
            }
        }
        
        return dp[k][0];
    }
};
