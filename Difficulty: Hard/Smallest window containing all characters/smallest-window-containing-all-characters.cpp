class Solution {
  public:
    string minWindow(string &s, string &p) {
        int n = s.size();
        vector<int> f(26, 0); 
        int minLen = INT_MAX;
        int resStart = 0;

        for (char ch : p) f[ch - 'a']++;

        int count = p.size();
        int l = 0;

        for (int r = 0; r < n; r++) {
            char ch = s[r];
            if (f[ch - 'a'] > 0) count--;
            f[ch - 'a']--;

            while (count == 0) {
                if (r - l + 1 < minLen) {
                    minLen = r - l + 1;
                    resStart = l;
                }

                char ch2 = s[l];
                f[ch2 - 'a']++;
                if (f[ch2 - 'a'] > 0) count++;
                l++;
            }
        }

        return minLen == INT_MAX ? "" : s.substr(resStart, minLen);
        
    }
};