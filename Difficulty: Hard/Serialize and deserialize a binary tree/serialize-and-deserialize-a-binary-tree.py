from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            curr = queue.popleft()
            
            if curr:
                result.append(curr.data)
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                # Use -1 as a placeholder for null nodes
                result.append(-1)
                
        return result

    # Function to deserialize a list and return the root of the tree.
    def deSerialize(self, arr):
        if not arr:
            return None
        
        root = Node(arr[0])
        queue = deque([root])
        i = 1
        
        while queue and i < len(arr):
            curr = queue.popleft()
            
            # Process left child
            if arr[i] != -1:
                curr.left = Node(arr[i])
                queue.append(curr.left)
            i += 1
            
            # Process right child (check bounds for safety)
            if i < len(arr) and arr[i] != -1:
                curr.right = Node(arr[i])
                queue.append(curr.right)
            i += 1
            
        return root