class Solution:
    def minSwaps(self, arr):
        n = len(arr)
        inorder = []
        
        # 1. Perform Inorder Traversal on the Complete Binary Tree
        # Complete Binary Tree indices: Left = 2*i + 1, Right = 2*i + 2
        def get_inorder(index):
            if index >= n:
                return
            get_inorder(2 * index + 1)
            inorder.append(arr[index])
            get_inorder(2 * index + 2)
            
        get_inorder(0)
        
        # 2. Find minimum swaps to sort the 'inorder' array
        # Create a list of pairs (value, original_index)
        indexed_inorder = []
        for i in range(n):
            indexed_inorder.append([inorder[i], i])
            
        # Sort based on values to see where elements SHOULD be
        indexed_inorder.sort()
        
        swaps = 0
        visited = [False] * n
        
        for i in range(n):
            # If already visited or already in correct position, skip
            if visited[i] or indexed_inorder[i][1] == i:
                continue
            
            # Count the size of the cycle
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                # Move to the index where this element's value belongs
                curr = indexed_inorder[curr][1]
                cycle_size += 1
            
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps