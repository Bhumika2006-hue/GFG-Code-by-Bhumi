class Solution:
    def distCandy(self, root):
        self.moves = 0
        
        def balance(node):
            if not node:
                return 0
            
            # Recursively find the balance of left and right subtrees
            left_balance = balance(node.left)
            right_balance = balance(node.right)
            
            # The number of moves needed to resolve the subtrees' balances
            # is the absolute value of their excess or deficit.
            self.moves += abs(left_balance) + abs(right_balance)
            
            # Return the balance of the current subtree:
            # (Candies in current node + balance from children) - 1 (for current node)
            return node.data + left_balance + right_balance - 1
            
        balance(root)
        return self.moves