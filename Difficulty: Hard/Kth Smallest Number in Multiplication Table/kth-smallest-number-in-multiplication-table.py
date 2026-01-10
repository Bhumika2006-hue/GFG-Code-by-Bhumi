class Solution():
    def kthSmallest(self, n, m, k):
        def count_less_equal(mid):
            count = 0
            for i in range(1, n + 1):
                # In row i, elements are i, 2i, 3i... mi
                # We need i * j <= mid  => j <= mid / i
                # But j cannot exceed the number of columns m
                count += min(m, mid // i)
            return count

        low = 1
        high = n * m
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            # If there are at least k elements <= mid, 
            # then the kth smallest could be mid or something smaller
            if count_less_equal(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                # Need a larger number to reach k elements
                low = mid + 1
                
        return ans