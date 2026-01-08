import sys

class Solution:
    def maxPathSum(self, root):
        # We use a list to keep track of the maximum sum because 
        # integers are immutable and cannot be modified inside helper easily.
        self.max_sum = -float('inf')
        
        def solve(node):
            if node is None:
                return -float('inf')
            
            # Base case: If it's a leaf node (special node)
            if node.left is None and node.right is None:
                return node.data
            
            # Recursive calls for left and right subtrees
            l_sum = solve(node.left)
            r_sum = solve(node.right)
            
            # If current node has both children, it can be a bridge
            if node.left and node.right:
                # Update global maximum with path from leaf to leaf
                self.max_sum = max(self.max_sum, l_sum + r_sum + node.data)
                # Return the maximum branch to the parent
                return max(l_sum, r_sum) + node.data
            
            # If one child is missing, return the path through the existing child
            return (l_sum if node.left else r_sum) + node.data

        res = solve(root)
        
        # If the root itself was missing a child, the bridge logic in 'solve'
        # might not have triggered. We check if max_sum was updated.
        if self.max_sum == -float('inf'):
            return res
            
        return self.max_sum