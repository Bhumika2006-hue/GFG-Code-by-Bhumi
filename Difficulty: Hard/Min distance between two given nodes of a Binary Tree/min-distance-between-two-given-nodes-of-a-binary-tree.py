class Solution:
    def findDist(self, root, a, b):
        # 1. Helper function to find the Lowest Common Ancestor
        def findLCA(node, n1, n2):
            if not node or node.data == n1 or node.data == n2:
                return node
            
            left = findLCA(node.left, n1, n2)
            right = findLCA(node.right, n1, n2)
            
            if left and right:
                return node
            return left if left else right

        # 2. Helper function to find distance of a value from a given source
        def getDist(node, target, distance):
            if not node:
                return -1
            if node.data == target:
                return distance
            
            # Check left subtree
            left_dist = getDist(node.left, target, distance + 1)
            if left_dist != -1:
                return left_dist
                
            # Check right subtree
            return getDist(node.right, target, distance + 1)

        # Main execution
        lca = findLCA(root, a, b)
        d1 = getDist(lca, a, 0)
        d2 = getDist(lca, b, 0)
        
        return d1 + d2