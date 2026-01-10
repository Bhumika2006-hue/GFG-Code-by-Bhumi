import sys

class Solution:
    def minSubtreeSumBST(self, target, root):
        self.min_nodes = float('inf')

        def solve(node):
            if not node:
                # [isBST, sum, size, minVal, maxVal]
                return [True, 0, 0, float('inf'), float('-inf')]

            left = solve(node.left)
            right = solve(node.right)

            curr_res = [False, 0, 0, 0, 0]
            
            # Check BST conditions
            if left[0] and right[0] and left[4] < node.data < right[3]:
                curr_res[0] = True
                curr_res[1] = left[1] + right[1] + node.data
                curr_res[2] = left[2] + right[2] + 1
                curr_res[3] = min(node.data, left[3])
                curr_res[4] = max(node.data, right[4])

                # If it's a BST and sum matches target, update global minimum size
                if curr_res[1] == target:
                    self.min_nodes = min(self.min_nodes, curr_res[2])
            
            return curr_res

        solve(root)
        return self.min_nodes if self.min_nodes != float('inf') else -1