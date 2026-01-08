import sys

# Increase recursion depth for deep DSU trees
sys.setrecursionlimit(200000)

class Solution:
    def find(self, parent, i):
        if parent[i] == i:
            return i
        parent[i] = self.find(parent, parent[i])
        return parent[i]

    def jobSequencing(self, deadline, profit):
        # 1. Sort jobs by profit in descending order
        jobs = sorted(zip(deadline, profit), key=lambda x: x[1], reverse=True)
        
        n = len(deadline)
        max_deadline = max(deadline)
        
        # 2. Initialize DSU parent array
        # parent[i] will store the latest available slot <= i
        parent = list(range(max_deadline + 1))
        
        count_jobs = 0
        total_profit = 0
        
        for d, p in jobs:
            # 3. Use DSU to find the available slot for deadline 'd'
            available_slot = self.find(parent, d)
            
            # If available_slot is 0, it means no slots are free before the deadline
            if available_slot > 0:
                # Schedule the job in available_slot
                count_jobs += 1
                total_profit += p
                
                # 4. Union: Link this slot to the one before it (available_slot - 1)
                parent[available_slot] = self.find(parent, available_slot - 1)
                    
        return [count_jobs, total_profit]