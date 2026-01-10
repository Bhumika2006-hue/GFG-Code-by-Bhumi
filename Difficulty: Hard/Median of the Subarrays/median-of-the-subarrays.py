class Solution:
    def countSubarray(self, N, A, M):
        
        def countAtLeast(X):
            # Count subarrays where median >= X
            # Transformation: elements >= X are 1, elements < X are -1
            # We need sum of subarray > 0
            
            # Since the prefix sum range is [-N, N], we use an offset to map
            # it to [0, 2*N] for a frequency array (faster than a dictionary)
            offset = N
            count_map = [0] * (2 * N + 1)
            count_map[offset] = 1 # Initial prefix sum 0
            
            current_sum = 0
            subarrays = 0
            total_elements_seen = 0 # This helps count prefixes smaller than current
            
            # To do this in O(N), we keep track of how many prefix sums
            # encountered so far are smaller than the current current_sum.
            smaller_sums_count = 0
            
            for val in A:
                if val >= X:
                    # current_sum increases: all previous sums stay smaller, 
                    # plus the count of the sum we just stepped over
                    smaller_sums_count += count_map[current_sum + offset]
                    current_sum += 1
                else:
                    # current_sum decreases: we lose the count of the 
                    # new sum we just landed on
                    current_sum -= 1
                    smaller_sums_count -= count_map[current_sum + offset]
                
                subarrays += smaller_sums_count
                count_map[current_sum + offset] += 1
                
            return subarrays

        return countAtLeast(M) - countAtLeast(M + 1)