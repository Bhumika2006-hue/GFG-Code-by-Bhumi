class Solution {
  public:
  int solve(int n, vector<int>& dp) {
        // Base Case
        if (n == 0) return 0;
        
        // If already calculated, return the cached value
        if (dp[n] != -1) return dp[n];
        
        // Recursively calculate for n/2, n/3, and n/4
        int brokenSum = solve(n / 2, dp) + solve(n / 3, dp) + solve(n / 4, dp);
        
        // Store the maximum of keeping n intact or breaking it down
        return dp[n] = max(n, brokenSum);
    }
    int maxSum(int n) {
        
        vector<int> dp(n + 1, -1);
        return solve(n, dp);
    }
};