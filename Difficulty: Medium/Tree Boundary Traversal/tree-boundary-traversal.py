class Solution:
    def boundaryTraversal(self, root):
        if not root:
            return []
        
        def is_leaf(node):
            return node.left is None and node.right is None
            
        res = []
        
        # 1. Add Root (if it's not a leaf)
        if not is_leaf(root):
            res.append(root.data)
            
        # 2. Collect Left Boundary (excluding leaves)
        curr = root.left
        while curr:
            if not is_leaf(curr):
                res.append(curr.data)
            # Prefer left child; if not available, go right
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
                
        # 3. Collect Leaf Nodes (Iterative DFS to handle deep trees)
        # We use a stack to process nodes Left-to-Right
        stack = [root]
        while stack:
            node = stack.pop()
            if is_leaf(node):
                res.append(node.data)
            # Push right first so that left is popped and processed first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        # 4. Collect Right Boundary (excluding leaves, in reverse)
        right_boundary = []
        curr = root.right
        while curr:
            if not is_leaf(curr):
                right_boundary.append(curr.data)
            # Prefer right child; if not available, go left
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        
        # Add right boundary nodes in reverse order
        res.extend(right_boundary[::-1])
        
        return res