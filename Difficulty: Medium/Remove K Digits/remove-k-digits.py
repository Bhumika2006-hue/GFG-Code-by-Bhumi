
class Solution:
    def removeKdig(self, s, k):
        stack = []

        for ch in s:
            # Remove larger digits from stack if possible
            while stack and k > 0 and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        # If k digits still need to be removed, remove from end
        while k > 0 and stack:
            stack.pop()
            k -= 1

        # Remove leading zeros
        result = ''.join(stack).lstrip('0')

        # If empty, return "0"
        return result if result else "0"
