class Solution:
    def search(self, txt, pat):
        n = len(txt)
        m = len(pat)
        
        # 1. Create the combined string
        # S = pattern + sentinel + text
        S = pat + "$" + txt
        total_len = len(S)
        
        # 2. Compute the Z-array
        z = [0] * total_len
        l, r = 0, 0
        
        for i in range(1, total_len):
            # If i is within the current [l, r] window
            if i <= r:
                # Copy value from the prefix-relative position
                z[i] = min(r - i + 1, z[i - l])
            
            # Attempt to extend the match beyond the current [l, r]
            while i + z[i] < total_len and S[z[i]] == S[i + z[i]]:
                z[i] += 1
            
            # Update the [l, r] window if we found a match further to the right
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        
        # 3. Collect indices where Z[i] == length of pattern
        # The indices in the combined string S correspond to:
        # index in txt = i - (m + 1)
        ans = []
        for i in range(m + 1, total_len):
            if z[i] == m:
                ans.append(i - (m + 1))
        
        return ans