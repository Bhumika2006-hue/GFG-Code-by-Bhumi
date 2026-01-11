class Solution:
    def countSubarray(self, N, A, L, R):
        
        # Helper function to count subarrays with sum <= X
        def countSubarraysWithMaxSum(X):
            if X < 0:
                return 0
            
            count = 0
            current_sum = 0
            left = 0
            
            for right in range(N):
                current_sum += A[right]
                
                # Shrink window from left if sum exceeds X
                while current_sum > X and left <= right:
                    current_sum -= A[left]
                    left += 1
                
                # All subarrays starting from 'left' to 'right' 
                # ending at 'right' are valid
                count += (right - left + 1)
                
            return count

        # Result is (subarrays with sum <= R) - (subarrays with sum <= L-1)
        return countSubarraysWithMaxSum(R) - countSubarraysWithMaxSum(L - 1)