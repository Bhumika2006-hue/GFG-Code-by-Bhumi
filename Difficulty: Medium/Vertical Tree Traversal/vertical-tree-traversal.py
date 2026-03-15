from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root):
        if not root:
            return []
        
        mp = defaultdict(list)
        q = deque([(root, 0)])
        
        min_hd = max_hd = 0
        
        while q:
            node, hd = q.popleft()
            
            mp[hd].append(node.data)
            
            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)
            
            if node.left:
                q.append((node.left, hd - 1))
            
            if node.right:
                q.append((node.right, hd + 1))
        
        result = []
        
        for hd in range(min_hd, max_hd + 1):
            result.append(mp[hd])
        
        return result