class Solution:
    def sortedListToBST(self, head):
        # Step 1: Count the total number of nodes
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        
        # Use a list to store the head so it's mutable across recursive calls
        self.curr = head
        
        def construct_bst(count):
            # Base case
            if count <= 0:
                return None
            
            # Recursively build the left subtree
            left_subtree = construct_bst(count // 2)
            
            # Create the root node using the current head's data
            root = TNode(self.curr.data)
            root.left = left_subtree
            
            # Move the linked list pointer forward
            self.curr = self.curr.next
            
            # Recursively build the right subtree
            # Total nodes (count) - nodes in left - 1 (root)
            root.right = construct_bst(count - (count // 2) - 1)
            
            return root
            
        return construct_bst(n)