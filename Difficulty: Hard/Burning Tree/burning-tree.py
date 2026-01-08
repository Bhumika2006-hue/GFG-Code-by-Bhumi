from collections import deque

class Solution:
    def minTime(self, root, target):
        # Step 1: Map parents and find the target node object
        parent_map = {}
        target_node = None
        
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if curr.data == target:
                target_node = curr
            
            if curr.left:
                parent_map[curr.left] = curr
                queue.append(curr.left)
            if curr.right:
                parent_map[curr.right] = curr
                queue.append(curr.right)
        
        # Step 2: BFS to simulate the burning process
        # (node, current_time)
        fire_queue = deque([(target_node, 0)])
        visited = {target_node}
        max_time = 0
        
        while fire_queue:
            curr_node, time = fire_queue.popleft()
            max_time = max(max_time, time)
            
            # Explore all 3 directions: Left, Right, and Parent
            for neighbor in [curr_node.left, curr_node.right, parent_map.get(curr_node)]:
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    fire_queue.append((neighbor, time + 1))
                    
        return max_time