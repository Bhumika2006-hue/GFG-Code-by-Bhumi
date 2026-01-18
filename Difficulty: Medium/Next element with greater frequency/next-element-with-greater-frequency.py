from collections import Counter

class Solution:
    def nextFreqGreater(self, arr):
        n = len(arr)
        freq = Counter(arr)
        res = [-1] * n
        stack = []

        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            # Remove elements with frequency <= current
            while stack and freq[stack[-1]] <= freq[arr[i]]:
                stack.pop()

            # Top of stack has higher frequency
            if stack:
                res[i] = stack[-1]

            # Push current element
            stack.append(arr[i])

        return res
