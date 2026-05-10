class Solution {
public:
    int maxProfit(int x, int y, vector<int> &a, vector<int> &b) {
        int n = a.size();
        long long totalProfit = 0;
        vector<int> gains;

        for (int i = 0; i < n; i++) {
            totalProfit += b[i];
            gains.push_back(a[i] - b[i]);
        }

        sort(gains.rbegin(), gains.rend());

        int countA = 0;
        int mandatoryA = max(0, n - y);
        for (int i = 0; i < mandatoryA; i++) {
            totalProfit += gains[i];
            countA++;
        }

        for (int i = countA; i < x && i < n; i++) {
            if (gains[i] > 0) {
                totalProfit += gains[i];
            } else {
                break;
            }
        }

        return (int)totalProfit;
    }
};