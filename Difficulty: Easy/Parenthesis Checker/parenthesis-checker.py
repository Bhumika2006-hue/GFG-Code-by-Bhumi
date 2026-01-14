class Solution:
    def isBalanced(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()

        return len(stack) == 0
