class Solution {
public:
    vector<vector<int>> dp;
    
    set<string> solve(int i, int j, string path, const string& s1, const string& s2) {
        if (i == s1.size() || j == s2.size()) {
            return {path};
        }
        
        string key = to_string(i) + "," + to_string(j) + "," + path;
        if (memo.find(key) != memo.end()) {
            return memo[key];
        }
        
        set<string> result;
        
        if (s1[i] == s2[j]) {
            // Include this character
            auto sub = solve(i + 1, j + 1, path + s1[i], s1, s2);
            result.insert(sub.begin(), sub.end());
        } else {
            // Skip i
            if (dp[i + 1][j] == dp[i][j]) {
                auto sub1 = solve(i + 1, j, path, s1, s2);
                result.insert(sub1.begin(), sub1.end());
            }
            
            // Skip j  
            if (dp[i][j + 1] == dp[i][j]) {
                auto sub2 = solve(i, j + 1, path, s1, s2);
                result.insert(sub2.begin(), sub2.end());
            }
        }
        
        memo[key] = result;
        return result;
    }
    
    unordered_map<string, set<string>> memo;
    
    vector<string> allLCS(string &s1, string &s2) {
        int n = s1.size(), m = s2.size();
        
        // Build LCS length DP table
        dp.assign(n + 1, vector<int>(m + 1, 0));
        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                if (s1[i] == s2[j]) {
                    dp[i][j] = 1 + dp[i + 1][j + 1];
                } else {
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1]);
                }
            }
        }
        
        // Get all LCS of maximum length
        int lcsLen = dp[0][0];
        memo.clear();
        
        set<string> all = solve(0, 0, "", s1, s2);
        
        vector<string> ans;
        for (const string& s : all) {
            if ((int)s.size() == lcsLen) {
                ans.push_back(s);
            }
        }
        
        return ans;
    }
};

