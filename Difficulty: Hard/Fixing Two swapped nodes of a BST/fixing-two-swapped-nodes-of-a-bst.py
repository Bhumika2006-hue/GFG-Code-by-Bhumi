class Solution:
    def correctBST(self, root):
        # Initializing pointers to track the swapped nodes
        self.first = None
        self.middle = None
        self.last = None
        self.prev = None
        
        def inorder(node):
            if not node:
                return
            
            # Left Subtree
            inorder(node.left)
            
            # Process Current Node
            if self.prev:
                # If current node is smaller than previous, violation detected
                if node.data < self.prev.data:
                    # If this is the first violation
                    if not self.first:
                        self.first = self.prev
                        self.middle = node
                    # If this is the second violation
                    else:
                        self.last = node
            
            self.prev = node
            
            # Right Subtree
            inorder(node.right)
            
        # Perform traversal
        inorder(root)
        
        # Swap the data of the two identified nodes
        if self.first and self.last:
            # Case: Non-adjacent nodes swapped
            self.first.data, self.last.data = self.last.data, self.first.data
        elif self.first and self.middle:
            # Case: Adjacent nodes swapped
            self.first.data, self.middle.data = self.middle.data, self.first.data
            
        return root