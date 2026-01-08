class Solution:
    def __init__(self):
        self.first = None
        self.middle = None # To handle adjacent swapped nodes
        self.last = None
        self.prev = None

    def inorder(self, root):
        if not root:
            return
        
        self.inorder(root.left)
        
        # Check for violation
        if self.prev and root.data < self.prev.data:
            # If this is the first violation, mark prev and current
            if not self.first:
                self.first = self.prev
                self.middle = root
            # If this is the second violation, mark current
            else:
                self.last = root
        
        self.prev = root
        self.inorder(root.right)

    def correctBST(self, root):
        # Reset pointers for each call
        self.first = self.middle = self.last = self.prev = None
        
        # Perform traversal to find swapped nodes
        self.inorder(root)
        
        # Swap values back
        if self.first and self.last:
            # Nodes were far apart
            self.first.data, self.last.data = self.last.data, self.first.data
        elif self.first and self.middle:
            # Nodes were adjacent in inorder traversal
            self.first.data, self.middle.data = self.middle.data, self.first.data
        
        return root