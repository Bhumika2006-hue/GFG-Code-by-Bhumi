class Solution():
    def countSubstring(self, S):
        n = len(S)
        # Shift to handle negative prefix sums (min sum is -n, max is n)
        offset = n
        # count_array stores how many times each prefix sum has occurred
        count_array = [0] * (2 * n + 1)
        
        curr_sum = 0
        ans = 0
        valid_subarrays = 0
        
        # Initial state: prefix sum 0 has occurred once
        count_array[offset] = 1
        
        for char in S:
            if char == '1':
                # Sum increases: all previous subarrays ending here that were 
                # valid remain valid, and those that were exactly 0 now become 1.
                # Specifically, we add the count of the previous curr_sum.
                valid_subarrays += count_array[curr_sum + offset]
                curr_sum += 1
            else:
                # Sum decreases: we lose the subarrays that had a sum of 1 
                # (they now become 0).
                curr_sum -= 1
                valid_subarrays -= count_array[curr_sum + offset]
            
            ans += valid_subarrays
            count_array[curr_sum + offset] += 1
            
        return ans