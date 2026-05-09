class Solution {
  public:
    int countSpanTree(int n, vector<vector<int>>& edges) {
         if (n <= 1) return 1;

        vector<vector<double>> laplacian(n, vector<double>(n, 0));

        for (auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            laplacian[u][u]++;
            laplacian[v][v]++;
            laplacian[u][v]--;
            laplacian[v][u]--;
        }

        int size = n - 1;
        vector<vector<double>> matrix(size, vector<double>(size));
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                matrix[i][j] = laplacian[i][j];
            }
        }

        double det = 1;
        for (int i = 0; i < size; i++) {
            int pivot = i;
            for (int j = i + 1; j < size; j++) {
                if (abs(matrix[j][i]) > abs(matrix[pivot][i])) pivot = j;
            }
            
            if (pivot != i) {
                swap(matrix[i], matrix[pivot]);
                det *= -1;
            }

            if (abs(matrix[i][i]) < 1e-9) return 0;

            det *= matrix[i][i];
            for (int j = i + 1; j < size; j++) {
                double factor = matrix[j][i] / matrix[i][i];
                for (int k = i + 1; k < size; k++) {
                    matrix[j][k] -= factor * matrix[i][k];
                }
            }
        }

        return (int)round(abs(det));
    }
};