class Solution {
  public:
    int derangeCount(int n) {
        // code here
        if (n == 0)
            return 1;
        if (n == 1)
            return 0;
        if (n == 2)
            return 1;
        long long prev2 = 0;
        long long prev1 = 1;
        long long cur = 0;
        for (int i = 3; i <= n; i++){
            cur = 1LL * (i - 1) * (prev1 + prev2);
            prev2 = prev1;
            prev1 = cur;
        }
        return (int)prev1;
    }
};