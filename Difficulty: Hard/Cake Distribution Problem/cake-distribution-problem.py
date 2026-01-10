class Solution():
    def maxSweetness(self, sweetness, n, k):
        # We need to divide the cake into K + 1 pieces
        target_pieces = k + 1
        
        def can_distribute(min_allowed_sweetness):
            pieces_count = 0
            current_sum = 0
            for s in sweetness:
                current_sum += s
                # If this piece reaches the threshold, cut it
                if current_sum >= min_allowed_sweetness:
                    pieces_count += 1
                    current_sum = 0
            # Return true if we can get at least target_pieces
            return pieces_count >= target_pieces

        # Binary search range
        low = min(sweetness)
        high = sum(sweetness) // target_pieces
        ans = low

        while low <= high:
            mid = (low + high) // 2
            
            if can_distribute(mid):
                # If we can satisfy everyone with at least 'mid' sweetness,
                # try for a larger value.
                ans = mid
                low = mid + 1
            else:
                # 'mid' is too large, reduce the requirement
                high = mid - 1
                
        return ans