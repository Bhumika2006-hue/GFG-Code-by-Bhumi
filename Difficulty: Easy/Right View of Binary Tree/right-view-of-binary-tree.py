from collections import deque

class Solution:
    def rightView(self, root):
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            level_size = len(q)

            for i in range(level_size):
                node = q.popleft()

                # Last node of each level
                if i == level_size - 1:
                    result.append(node.data)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return result
