class Solution {
public:
    int waysToIncreaseLCSBy1(string s1, string s2) {
        int n = s1.length();
        int m = s2.length();
        
        // pref[i][j] stores the LCS of s1[0...i-1] and s2[0...j-1]
        vector<vector<int>> pref(n + 1, vector<int>(m + 1, 0));
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (s1[i - 1] == s2[j - 1]) {
                    pref[i][j] = 1 + pref[i - 1][j - 1];
                } else {
                    pref[i][j] = max(pref[i - 1][j], pref[i][j - 1]);
                }
            }
        }
        
        // suff[i][j] stores the LCS of s1[i-1...n-1] and s2[j-1...m-1]
        // Sized slightly larger to prevent out-of-bounds when shifting indices
        vector<vector<int>> suff(n + 2, vector<int>(m + 2, 0));
        for (int i = n; i >= 1; i--) {
            for (int j = m; j >= 1; j--) {
                if (s1[i - 1] == s2[j - 1]) {
                    suff[i][j] = 1 + suff[i + 1][j + 1];
                } else {
                    suff[i][j] = max(suff[i + 1][j], suff[i][j + 1]);
                }
            }
        }
        
        int L = pref[n][m]; // Original LCS length
        int ans = 0;
        
        // Iterate over all possible insertion positions in s1 (0 to n)
        for (int i = 0; i <= n; i++) {
            bool used[26] = {false}; // Prevent double-counting characters at the same insertion point
            
            // Try matching our inserted character with s2[j]
            for (int j = 0; j < m; j++) {
                int c = s2[j] - 'a';
                
                if (!used[c]) {
                    // Check if inserting s2[j] at position i forms an LCS of length L + 1
                    if (pref[i][j] + suff[i + 1][j + 2] == L) {
                        used[c] = true;
                        ans++;
                    }
                }
            }
        }
        
        return ans;
    }
};