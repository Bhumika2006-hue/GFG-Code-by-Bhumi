from typing import List

class Solution:
    def minTime(self, n: int, locations: List[int], types: List[int]) -> int:
        # Step 1: Group min and max locations for each type
        fruit_map = {}
        for loc, t in zip(locations, types):
            if t not in fruit_map:
                fruit_map[t] = [loc, loc]
            else:
                fruit_map[t][0] = min(fruit_map[t][0], loc)
                fruit_map[t][1] = max(fruit_map[t][1], loc)
        
        # Step 2: Sort types to process them in non-decreasing order
        sorted_types = sorted(fruit_map.keys())
        
        # We add a dummy type at the end to represent returning to 0
        # This simplifies the logic
        unique_locs = []
        for t in sorted_types:
            unique_locs.append(fruit_map[t])
        unique_locs.append([0, 0])
        
        # dp[0] = min time ending at current type's MIN location
        # dp[1] = min time ending at current type's MAX location
        # Initial position is 0
        curr_min_pos, curr_max_pos = 0, 0
        dp = [0, 0]
        
        for next_min, next_max in unique_locs:
            # Distance needed to cover all fruits of the NEW type
            dist_of_new_type = next_max - next_min
            
            # Option 1: End at next_min
            # This means we must have arrived at next_max first, then traversed to next_min
            to_min = min(
                dp[0] + abs(curr_min_pos - next_max) + dist_of_new_type,
                dp[1] + abs(curr_max_pos - next_max) + dist_of_new_type
            )
            
            # Option 2: End at next_max
            # This means we must have arrived at next_min first, then traversed to next_max
            to_max = min(
                dp[0] + abs(curr_min_pos - next_min) + dist_of_new_type,
                dp[1] + abs(curr_max_pos - next_min) + dist_of_new_type
            )
            
            dp = [to_min, to_max]
            curr_min_pos, curr_max_pos = next_min, next_max
            
        # The result is stored in dp[0] (or dp[1]) after the dummy [0,0] type
        return dp[0]