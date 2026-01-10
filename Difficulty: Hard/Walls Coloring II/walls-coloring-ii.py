from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        
        n = len(costs)
        k = len(costs[0])
        
        # If there's more than one wall but only one color, it's impossible
        if k == 1 and n > 1:
            return -1
        if k == 0:
            return -1

        # prev_min1: smallest cost to paint previous walls
        # prev_min2: second smallest cost to paint previous walls
        # prev_idx: the color index that resulted in prev_min1
        prev_min1, prev_min2, prev_idx = 0, 0, -1
        
        for i in range(n):
            curr_min1, curr_min2, curr_idx = float('inf'), float('inf'), -1
            
            for j in range(k):
                # Calculate cost for current wall with color j
                # Use prev_min1 if color j != prev_idx, else use prev_min2
                current_total = costs[i][j] + (prev_min2 if j == prev_idx else prev_min1)
                
                # Update the current two minimums
                if current_total < curr_min1:
                    curr_min2 = curr_min1
                    curr_min1 = current_total
                    curr_idx = j
                elif current_total < curr_min2:
                    curr_min2 = current_total
            
            # Move current minimums to previous for next wall
            prev_min1, prev_min2, prev_idx = curr_min1, curr_min2, curr_idx
            
        return prev_min1