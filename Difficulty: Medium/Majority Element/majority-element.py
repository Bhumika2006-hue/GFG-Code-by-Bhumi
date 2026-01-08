class Solution:
    def majorityElement(self, arr):
        n = len(arr)
        candidate = None
        count = 0
        
        # Phase 1: Find the potential candidate
        for num in arr:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        
        # Phase 2: Verify the candidate
        actual_count = 0
        for num in arr:
            if num == candidate:
                actual_count += 1
        
        # Check if candidate is actually the majority
        if actual_count > n // 2:
            return candidate
        else:
            return -1