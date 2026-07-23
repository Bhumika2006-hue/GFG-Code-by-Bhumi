class Solution:
    def canRepresentBST(self, arr):
        stack = []
        lower_bound = float('-inf')

        for x in arr:
            if x < lower_bound:
                return False

            while stack and x > stack[-1]:
                lower_bound = stack.pop()

            stack.append(x)

        return True