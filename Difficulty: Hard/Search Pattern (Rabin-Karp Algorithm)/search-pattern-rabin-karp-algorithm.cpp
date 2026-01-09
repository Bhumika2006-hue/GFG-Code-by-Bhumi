class Solution {
  public:
    vector<int> rabinKarp(string &text, string &pattern) {
        vector<int> result;
        int n = text.size();
        int m = pattern.size();
        
        if (m == 0 || n == 0) return result;
        if (m > n) return result;
        
        // Prime number and base for rolling hash
        const long long p = 31;
        const long long mod = 1e9 + 9;
        
        // Precompute powers of p
        vector<long long> powP(m + 1, 1);
        for (int i = 1; i <= m; i++) {
            powP[i] = (powP[i - 1] * p) % mod;
        }
        
        // Hash of pattern
        long long patHash = 0;
        for (int i = 0; i < m; i++) {
            patHash = (patHash * p + (pattern[i] - 'a' + 1)) % mod;
        }
        
        // Hash of first window in text
        long long txtHash = 0;
        for (int i = 0; i < m; i++) {
            txtHash = (txtHash * p + (text[i] - 'a' + 1)) % mod;
        }
        
        // Slide window
        for (int i = 0; i <= n - m; i++) {
            // Compare hashes
            if (txtHash == patHash) {
                // Verify actual strings (avoid hash collision)
                if (text.substr(i, m) == pattern) {
                    result.push_back(i);
                }
            }
            
            // Calculate next window hash
            if (i < n - m) {
                // Remove first char: txtHash = txtHash - text[i] * p^(m-1)
                txtHash = (txtHash - (text[i] - 'a' + 1) * powP[m - 1] % mod + mod) % mod;
                // Add next char
                txtHash = (txtHash * p + (text[i + m] - 'a' + 1)) % mod;
            }
        }
        
        return result;
    }
};
