class Solution {
  public:
    int celebrity(vector<vector<int>>& mat) {
        int n = mat.size();
        int top = 0, down = n - 1;

        while (top < down) {
            if (mat[top][down] == 1)
                top++;
            else
                down--;
        }
        int j = top;

        for (int i = 0; i < n; i++) {
            if (i != j) {
                if (mat[j][i] != 0 || mat[i][j] != 1) {
                    return -1;
                }
            }
        }
        return j;
    }
};