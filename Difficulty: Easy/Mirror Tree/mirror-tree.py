class Solution:
    def mirror(self, root):
        if root is None:
            return
        
        # Swap left and right children
        root.left, root.right = root.right, root.left
        
        # Recur for left and right subtrees
        self.mirror(root.left)
        self.mirror(root.right)
