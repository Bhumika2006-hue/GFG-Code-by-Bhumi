class Solution {
    public int countSquare(int[][] mat, int x) {
    
    int n = mat.length;
        int m = mat[0].length;
        int[][] ps = new int[n + 1][m + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                ps[i][j] = mat[i - 1][j - 1]
                        + ps[i - 1][j]
                        + ps[i][j - 1]
                        - ps[i - 1][j - 1];
            }
        }

        int count = 0;
        int maxSize = Math.min(n, m);
        for (int size = 1; size <= maxSize; size++) {
            for (int i = 0; i + size - 1 < n; i++) {
                for (int j = 0; j + size - 1 < m; j++) {

                    int r2 = i + size - 1;
                    int c2 = j + size - 1;

                    int sum = ps[r2 + 1][c2 + 1]
                            - ps[i][c2 + 1]
                            - ps[r2 + 1][j]
                            + ps[i][j];

                    if (sum == x) count++;
                }
            }
        }

        return count;
        
    }
}