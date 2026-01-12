class Solution():
    def minSprinkler(self, arr, n):
        # Step 1: Create a jump array (max_reach)
        # jump[i] stores the furthest right point reachable from point i
        jump = [i for i in range(n + 1)]
        
        for i in range(1, n + 1):
            # 1-based index i means arr index is i-1
            left = max(1, i - arr[i-1])
            right = min(n, i + arr[i-1])
            # For the starting point 'left', the furthest we can go is 'right'
            jump[left] = max(jump[left], right)
            
        # Step 2: Update jump array to handle starting at or before point i
        # If we can reach 'X' from point i, we can also reach 'X' from point i+1
        # This is essentially a prefix maximum logic for the starts.
        curr_max = 0
        for i in range(1, n + 1):
            curr_max = max(curr_max, jump[i])
            jump[i] = curr_max
            
        # Step 3: Greedy traversal to count sprinklers
        count = 0
        current_end = 0 # Garden covered up to this point
        farthest = 0    # Maximum reachable point with one more sprinkler
        
        i = 1
        while i <= n:
            # While we are within the current coverage, find the best next sprinkler
            if i <= jump[i]:
                farthest = jump[i]
            
            # If the current best sprinkler doesn't even reach our current position,
            # it's impossible to cover the garden.
            if farthest < i:
                return -1
                
            count += 1
            # Move our coverage to the farthest possible point
            current_end = farthest
            i = current_end + 1
            
        return count