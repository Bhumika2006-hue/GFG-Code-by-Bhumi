class Item:
    def __init__(self, val, wt):
        self.val = val
        self.wt = wt
        self.ratio = val / wt

class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        n = len(val)
        items = []
        
        # Create a list of items with their value-to-weight ratios
        for i in range(n):
            items.append(Item(val[i], wt[i]))
            
        # Sort items based on ratio in descending order
        items.sort(key=lambda x: x.ratio, reverse=True)
        
        total_value = 0.0
        current_capacity = capacity
        
        for item in items:
            if current_capacity == 0:
                break
                
            if item.wt <= current_capacity:
                # Take the full item
                total_value += item.val
                current_capacity -= item.wt
            else:
                # Take a fraction of the item to fill the remaining capacity
                total_value += item.ratio * current_capacity
                current_capacity = 0
                break
                
        return round(total_value, 6)