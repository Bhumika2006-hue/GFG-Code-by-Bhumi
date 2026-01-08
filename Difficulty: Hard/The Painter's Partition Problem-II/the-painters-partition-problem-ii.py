class Solution:
    def minTime(self, arr, k):
        # n is the number of boards
        n = len(arr)
        
        # If there are more painters than boards, the time taken 
        # is just the length of the longest board.
        low = max(arr)
        high = sum(arr)
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check if it's possible to paint all boards within 'mid' time
            if self.is_possible(arr, n, k, mid):
                ans = mid  # This is a potential answer, try to find a smaller one
                high = mid - 1
            else:
                low = mid + 1
                
        return ans

    def is_possible(self, arr, n, k, limit):
        painters_count = 1
        current_sum = 0
        
        for board in arr:
            if current_sum + board <= limit:
                current_sum += board
            else:
                # Assign to a new painter
                painters_count += 1
                current_sum = board
                
                # If required painters exceed available k, return False
                if painters_count > k:
                    return False
                    
        return True