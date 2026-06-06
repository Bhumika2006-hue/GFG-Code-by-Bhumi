class Solution {
public:
    int numOfWays(int n, int m) {

        // code here
        vector<int> da = {2, 2, -2, -2, 1, 1, -1, -1};
        vector<int> db = {1, -1, 1, -1, 2, -2, 2, -2};

        int ans = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {

                int count = 1;

                for (int d = 0; d < 8; d++) {

                    int ni = i + da[d];
                    int nj = j + db[d];

                    if (ni >= 0 && nj >= 0 && ni < n && nj < m) {
                        count++;
                    }
                }

                ans += (n * m) - count;
            }
        }

        return ans;
    }
};