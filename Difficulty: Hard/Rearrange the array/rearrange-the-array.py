import math

class Solution:
    def rearrangeArray(self, n, arr):
        visited = [False] * (n + 1)
        cycle_lengths = []
        
        # Adjust arr to be 0-indexed for easier calculation 
        # (subtract 1 from each element if it's 1-indexed)
        # The example implies arr[i] is the destination index.
        # Let's assume the input arr is 1-indexed as per "1 to N".
        
        adj = [x - 1 for x in arr]
        
        for i in range(n):
            if not visited[i]:
                count = 0
                curr = i
                while not visited[curr]:
                    visited[curr] = True
                    curr = adj[curr]
                    count += 1
                cycle_lengths.append(count)
        
        # Calculate LCM of all cycle lengths
        ans = 1
        for length in cycle_lengths:
            ans = (ans * length) // math.gcd(ans, length)
            
        return ans % 1000000007