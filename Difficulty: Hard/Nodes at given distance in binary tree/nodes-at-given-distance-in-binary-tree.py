from collections import deque

class Solution:
    def KDistanceNodes(self, root, target, k):
        # 1. Map parents and find target node object
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
        
        # 2. Radial BFS from target node
        res = []
        queue = deque([(target_node, 0)])
        visited = {target_node}
        
        while queue:
            curr, dist = queue.popleft()
            
            if dist == k:
                res.append(curr.data)
                # All other nodes in queue at this level will also be at distance k
                while queue:
                    node, d = queue.popleft()
                    if d == k:
                        res.append(node.data)
                break
            
            # Explore neighbors: Left, Right, and Parent
            for neighbor in [curr.left, curr.right, parent_map.get(curr)]:
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        
        # 3. Return sorted results
        return sorted(res)