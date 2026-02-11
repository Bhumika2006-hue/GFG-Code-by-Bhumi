class Solution:
    def minCost(self, heights, cost):
        # Pair heights with their costs
        towers = list(zip(heights, cost))
        
        # Sort by height
        towers.sort()
        
        # Total cost (weight)
        total_weight = sum(cost)
        half_weight = (total_weight + 1) // 2
        
        # Find weighted median
        curr_weight = 0
        target_height = 0
        for h, c in towers:
            curr_weight += c
            if curr_weight >= half_weight:
                target_height = h
                break
        
        # Compute minimum cost
        min_cost = 0
        for h, c in towers:
            min_cost += abs(h - target_height) * c
        
        return min_cost
