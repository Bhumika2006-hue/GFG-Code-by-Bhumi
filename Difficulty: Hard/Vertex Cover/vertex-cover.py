from typing import List

class Solution:
    def vertexCover(self, n: int, edges: List[List[int]]) -> int:
        # We iterate through all possible subsets of vertices using a bitmask
        # There are 2^n total combinations
        min_size = n
        
        # Pre-process edges to use 0-indexing
        processed_edges = []
        for u, v in edges:
            processed_edges.append((u - 1, v - 1))
            
        # Iterate through all combinations from size 0 to n
        # Optimization: We can check masks with fewer set bits first to find min_size
        for i in range(1 << n):
            # count number of set bits (size of current vertex cover candidate)
            count = bin(i).count('1')
            
            # If current mask size is already worse than min_size, skip validation
            if count >= min_size:
                continue
                
            is_valid = True
            for u, v in processed_edges:
                # Check if neither endpoint of the edge is in the current mask
                if not ((i & (1 << u)) or (i & (1 << v))):
                    is_valid = False
                    break
            
            if is_valid:
                min_size = count
                
        return min_size