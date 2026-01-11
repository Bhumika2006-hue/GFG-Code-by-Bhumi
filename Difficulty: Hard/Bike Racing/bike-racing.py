class Solution:	
    def buzzTime(self, N, M, L, H, A):
        # Binary search for the minimum hour
        low = 0
        high = max(L, M) # A safe upper bound for time
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check if alarm buzzes at time 'mid'
            total_speed = 0
            for i in range(N):
                current_speed = H[i] + (A[i] * mid)
                if current_speed >= L:
                    total_speed += current_speed
                
                # Optimization: break early if we already exceeded M
                if total_speed >= M:
                    break
            
            if total_speed >= M:
                ans = mid
                high = mid - 1 # Try to find a smaller time
            else:
                low = mid + 1 # Need more time
                
        return ans