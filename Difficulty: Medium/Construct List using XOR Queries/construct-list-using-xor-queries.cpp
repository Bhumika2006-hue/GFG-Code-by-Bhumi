class Solution {
public:
    vector<int> constructList(vector<vector<int>> &queries) {
        vector<int> ans;
        ans.push_back(0); // The array initially contains only a single value, 0.
        
        int cumulative_xor = 0;
        
        // Process queries in reverse order
        for (int i = queries.size() - 1; i >= 0; i--) {
            if (queries[i][0] == 1) {
                // If it's a Type-1 query, it affects all elements inserted BEFORE it
                cumulative_xor ^= queries[i][1];
            } else {
                // If it's a Type-0 query, this element is only affected 
                // by the XOR queries that came AFTER it.
                ans.push_back(queries[i][1] ^ cumulative_xor);
            }
        }
        
        // The initial 0 also needs to be XORed with all Type-1 queries
        ans[0] ^= cumulative_xor;
        
        // Sort the final list as required by the problem
        sort(ans.begin(), ans.end());
        
        return ans;
    }
};