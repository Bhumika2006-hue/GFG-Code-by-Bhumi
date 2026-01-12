import heapq
from collections import deque

class Solution:
    def shortestRange(self, root):
        if not root:
            return [0, 0]
            
        # Step 1: Group nodes by levels using BFS
        levels = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level_nodes = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level_nodes.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Sorting each level helps the heap approach
            levels.append(sorted(current_level_nodes))
            
        # Step 2: Multi-way Merge / Heap approach
        # heap will store (value, level_index, element_index_in_that_level)
        min_heap = []
        max_val = float('-inf')
        
        for i in range(len(levels)):
            val = levels[i][0]
            heapq.heappush(min_heap, (val, i, 0))
            max_val = max(max_val, val)
            
        res_start, res_end = -1e9, 1e9
        
        while len(min_heap) == len(levels):
            min_val, level_idx, element_idx = heapq.heappop(min_heap)
            
            # Update best range
            if (max_val - min_val) < (res_end - res_start):
                res_start, res_end = min_val, max_val
            elif (max_val - min_val) == (res_end - res_start):
                if min_val < res_start:
                    res_start, res_end = min_val, max_val
            
            # If we can, push the next element from the same level into the heap
            if element_idx + 1 < len(levels[level_idx]):
                next_val = levels[level_idx][element_idx + 1]
                heapq.heappush(min_heap, (next_val, level_idx, element_idx + 1))
                max_val = max(max_val, next_val)
            else:
                # One level is exhausted, we cannot form a range covering all levels anymore
                break
                
        return [res_start, res_end]