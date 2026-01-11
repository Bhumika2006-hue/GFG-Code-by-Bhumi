class Solution:
    def checktree(self, preorder, inorder, postorder, N):
        # Index tracking for preorder traversal
        self.pre_idx = 0
        # Index tracking for postorder traversal
        self.post_idx = 0
        
        def solve(in_start, in_end):
            # Base case: empty subtree
            if in_start > in_end:
                return True
            
            # Root from preorder
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            
            # Find root in inorder to get subtree boundaries
            # Using index() is O(N), making total complexity O(N^2)
            try:
                root_in_idx = -1
                for i in range(in_start, in_end + 1):
                    if inorder[i] == root_val:
                        root_in_idx = i
                        break
                
                if root_in_idx == -1:
                    return False
            except ValueError:
                return False
                
            # Recursively check left subtree then right subtree
            if not solve(in_start, root_in_idx - 1):
                return False
            if not solve(root_in_idx + 1, in_end):
                return False
            
            # After subtrees are processed, the current root must match 
            # the current element in postorder (Post-order: Left, Right, Root)
            if postorder[self.post_idx] != root_val:
                return False
            
            self.post_idx += 1
            return True

        # Initial call
        result = solve(0, N - 1)
        
        # Final check: Did we process every node in the traversals?
        return result and self.pre_idx == N and self.post_idx == N