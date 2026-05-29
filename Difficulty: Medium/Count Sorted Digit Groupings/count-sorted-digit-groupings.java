class Solution {
    public int validGroups(String s) {
        int n = s.length();
        int ms = 9 * n;
        
        // Java equivalent of vector<vector<int>> v(n + 1, vector<int>(ms + 1, 0))
        int[][] v = new int[n + 1][ms + 1];
        
        // Base case initialization
        for (int j = 0; j <= ms; j++) {
            v[n][j] = 1;
        }
        
        // Iterative DP loops
        for (int i = n - 1; i >= 0; i--) {
            for (int p = 0; p <= ms; p++) {
                int sc = 0;
                for (int j = i; j < n; j++) {
                    sc += s.charAt(j) - '0'; // Use .charAt() instead of array indexing
                    if (sc >= p) {
                        v[i][p] += v[j + 1][sc];
                    }
                }
            }
        }
        
        return v[0][0];
    }
}