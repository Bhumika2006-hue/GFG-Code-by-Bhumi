class Solution:
    def palPartition(self, s):
        n = len(s)
        if n <= 1:
            return 0
            
        # Step 1: Precompute palindromes in O(n^2)
        # is_pal[i][j] is true if s[i...j] is a palindrome
        is_pal = [[False] * n for _ in range(n)]
        
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if length == 1:
                    is_pal[i][j] = True
                elif length == 2:
                    is_pal[i][j] = (s[i] == s[j])
                else:
                    is_pal[i][j] = (s[i] == s[j] and is_pal[i+1][j-1])
        
        # Step 2: Build the cuts DP array
        # cuts[i] = min cuts for substring s[0...i]
        cuts = [0] * n
        
        for i in range(n):
            if is_pal[0][i]:
                cuts[i] = 0
            else:
                # Initialize with maximum possible cuts (i cuts for i+1 chars)
                min_cut = i
                for j in range(i):
                    # If s[j+1...i] is a palindrome, try cutting after j
                    if is_pal[j+1][i]:
                        min_cut = min(min_cut, cuts[j] + 1)
                cuts[i] = min_cut
                
        return cuts[n-1]