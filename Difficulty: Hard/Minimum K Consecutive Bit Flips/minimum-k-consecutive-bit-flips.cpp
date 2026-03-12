class Solution {
  public:
    int kBitFlips(vector<int>& arr, int k) {
        // code here
   queue<int> q;
    int res = 0;
    int n = arr.size();

    for (int i = 0; i < n; i++) {
        // Remove flips that are out of current window 
        while (!q.empty() && i > q.front() + k - 1) {
            q.pop();
        }
        
        // If bit is 0 after considering flips done so far, flip at i
        if ((arr[i] + q.size()) % 2 == 0) {
            if (i + k > n) return -1; // Can't flip past array length
            res++;
            q.push(i); // Add this flip start index to queue
        }
    }
    return res;
    }
};