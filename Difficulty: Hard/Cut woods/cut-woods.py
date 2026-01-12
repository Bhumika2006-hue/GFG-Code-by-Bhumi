from typing import List

class Solution:
    def maxHeight(self, N : int, A : List[int], M : int) -> int:
        # Step 1: Define the search range for the blade height
        low = 0
        high = max(A)
        ans = 0
        
        # Step 2: Binary Search for the maximum height H
        while low <= high:
            mid = (low + high) // 2
            
            # Calculate total wood collected at height 'mid'
            total_wood = 0
            for height in A:
                if height > mid:
                    total_wood += (height - mid)
            
            # Step 3: Check if the wood collected meets the requirement
            if total_wood >= M:
                # We have enough wood, try to raise the blade further
                ans = mid
                low = mid + 1
            else:
                # Not enough wood, must lower the blade
                high = mid - 1
                
        return ans