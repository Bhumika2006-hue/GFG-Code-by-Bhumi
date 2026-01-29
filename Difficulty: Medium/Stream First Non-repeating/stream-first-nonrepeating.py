from collections import deque

class Solution:
    def firstNonRepeating(self, s):
        freq = [0] * 26
        q = deque()
        ans = []

        for ch in s:
            idx = ord(ch) - ord('a')
            freq[idx] += 1
            q.append(ch)

            # Remove repeating characters from front
            while q and freq[ord(q[0]) - ord('a')] > 1:
                q.popleft()

            if q:
                ans.append(q[0])
            else:
                ans.append('#')

        return "".join(ans)
