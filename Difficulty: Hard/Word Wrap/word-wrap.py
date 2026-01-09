class Solution:
    def solveWordWrap(self, arr, k):
        n = len(arr)
        # dp[i] will store the minimum cost for words from index i to n-1
        dp = [0] * n
        
        # Base case: The last word has 0 cost because it's in the last line
        dp[n-1] = 0
        
        # Iterate backwards from the second to last word
        for i in range(n - 2, -1, -1):
            curr_len = -1 # Start at -1 to handle the space logic easily
            min_cost = float('inf')
            
            # Try including words from i to j in the current line
            for j in range(i, n):
                # Calculate length: previous words + current word + 1 space
                curr_len += (arr[j] + 1)
                
                # If the words exceed the line width, we can't add more
                if curr_len > k:
                    break
                
                # If we are at the last word, the cost for this line is 0
                if j == n - 1:
                    cost = 0
                else:
                    # Cost = (extra spaces)^2 + min cost of remaining words
                    extra_spaces = k - curr_len
                    cost = (extra_spaces ** 2) + dp[j+1]
                
                if cost < min_cost:
                    min_cost = cost
            
            dp[i] = min_cost
            
        return dp[0]