class Solution:
    
    # Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        # We use a helper function to pass the valid range down
        # Using large constants for infinity to handle 10^9 constraints
        return self.validate(root, float('-inf'), float('inf'))
        
    def validate(self, node, min_val, max_val):
        # An empty tree is a valid BST
        if not node:
            return True
            
        # Current node's data must be strictly within the range
        if not (min_val < node.data < max_val):
            return False
            
        # Check subtrees:
        # Left child must be in range (min_val, current_node.data)
        # Right child must be in range (current_node.data, max_val)
        return (self.validate(node.left, min_val, node.data) and 
                self.validate(node.right, node.data, max_val))