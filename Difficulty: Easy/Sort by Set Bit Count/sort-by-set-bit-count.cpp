class Solution {
  public:
    vector<int> sortBySetBitCount(vector<int>& arr) {
        // code here
        auto countBits = [](int n) {
            int count = 0;
            while (n > 0) {
                n &= (n - 1);
                count++;
            }
            return count;
        };

        stable_sort(arr.begin(), arr.end(), [&](int a, int b) {
            return countBits(a) > countBits(b);
        });

        return arr;
    }
};