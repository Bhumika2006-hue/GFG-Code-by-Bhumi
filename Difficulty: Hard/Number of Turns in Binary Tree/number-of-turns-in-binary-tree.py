class Solution:
    def NumberOFTurns(self, root, first, second):
        # Step 1: Find LCA
        def findLCA(node, n1, n2):
            if not node: return None
            if node.data == n1 or node.data == n2:
                return node
            
            left = findLCA(node.left, n1, n2)
            right = findLCA(node.right, n1, n2)
            
            if left and right: return node
            return left if left else right

        # Step 2: Find path from node to target
        def getPath(node, target, path):
            if not node: return False
            if node.data == target: return True
            
            path.append('L')
            if getPath(node.left, target, path): return True
            path.pop()
            
            path.append('R')
            if getPath(node.right, target, path): return True
            path.pop()
            
            return False

        lca = findLCA(root, first, second)
        
        path1 = []
        path2 = []
        getPath(lca, first, path1)
        getPath(lca, second, path2)
        
        # Combine paths
        # path1 is LCA -> first, we need first -> LCA (reverse directions)
        # Note: In a tree, if you go from child to parent, 'L' remains 'L' 
        # in terms of the turn logic relative to the next move.
        full_path = ""
        
        # Path from first up to LCA (reverse the LCA->first path)
        # Directions stay same, we just process them in reverse order
        s1 = "".join(path1[::-1])
        s2 = "".join(path2)
        
        # If one node is LCA of other, the path is just s1 or s2
        full_path = s1 + s2
        
        if not full_path: return -1
        
        turns = 0
        for i in range(len(full_path) - 1):
            if full_path[i] != full_path[i+1]:
                turns += 1
        
        return turns if turns > 0 else -1