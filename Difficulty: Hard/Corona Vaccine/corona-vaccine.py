class Solution:
    def supplyVaccine(self, root):
        self.vaccines = 0
        
        # Helper function returns the state of the node
        # 0: Needs Coverage
        # 1: Has Vaccine
        # 2: Already Covered
        def dfs(node):
            if not node:
                # Null nodes are considered "Already Covered"
                return 2
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If any child needs coverage, this node MUST take a vaccine
            if left == 0 or right == 0:
                self.vaccines += 1
                return 1
            
            # If any child has a vaccine, this node is covered
            if left == 1 or right == 1:
                return 2
            
            # Otherwise, this node is not covered and has no vaccine
            # It waits for its parent to provide coverage
            return 0

        # Special case: If the root itself needs coverage
        if dfs(root) == 0:
            self.vaccines += 1
            
        return self.vaccines