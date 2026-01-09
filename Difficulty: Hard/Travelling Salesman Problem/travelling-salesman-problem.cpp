class Solution {
public:
    int tsp(vector<vector<int>>& cost) {
        int n = cost.size();
        
        // Base case: single city
        if (n == 1) return 0;
        
        vector<vector<int>> dp(1 << n, vector<int>(n, INT_MAX / 2));
        
        // Start from city 0
        dp[1][0] = 0;
        
        // Fill DP table
        for (int mask = 1; mask < (1 << n); mask++) {
            for (int u = 0; u < n; u++) {
                if ((mask & (1 << u)) == 0) continue;
                if (dp[mask][u] == INT_MAX / 2) continue;
                
                for (int v = 0; v < n; v++) {
                    if ((mask & (1 << v)) == 0) {
                        int newMask = mask | (1 << v);
                        dp[newMask][v] = min(dp[newMask][v], 
                                           dp[mask][u] + cost[u][v]);
                    }
                }
            }
        }
        
        // Return to city 0
        int ans = INT_MAX / 2;
        int fullMask = (1 << n) - 1;
        for (int u = 1; u < n; u++) {
            if (dp[fullMask][u] != INT_MAX / 2) {
                ans = min(ans, dp[fullMask][u] + cost[u][0]);
            }
        }
        
        return (ans == INT_MAX / 2) ? -1 : ans;  // -1 if impossible
    }
};
