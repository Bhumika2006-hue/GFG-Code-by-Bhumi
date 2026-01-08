from collections import deque

class Solution:
    def topView(self, root):
        if not root:
            return []
        
        # Dictionary to store the first node found at each horizontal distance
        # hd_map: {horizontal_distance: node_data}
        hd_map = {}
        
        # Queue for Level Order Traversal: (node, horizontal_distance)
        queue = deque([(root, 0)])
        
        # Track min and max HD to avoid sorting the map later (Optimization)
        min_hd, max_hd = 0, 0
        
        while queue:
            node, hd = queue.popleft()
            
            # If this horizontal distance is seen for the first time, 
            # it is the top-view node for this vertical line.
            if hd not in hd_map:
                hd_map[hd] = node.data
            
            # Update range for final result construction
            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)
            
            # standard BFS: left child gets (hd - 1), right gets (hd + 1)
            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Prepare the result from leftmost to rightmost
        result = []
        for i in range(min_hd, max_hd + 1):
            if i in hd_map:
                result.append(hd_map[i])
                
        return result