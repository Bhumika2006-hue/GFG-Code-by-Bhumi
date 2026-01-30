from collections import deque

class Solution:
    def rearrangeQueue(self, q):
        n = len(q)
        half = n // 2
        
        first = deque()
        
        # Step 1: Move first half into another queue
        for _ in range(half):
            first.append(q.popleft())
        
        # Step 2: Interleave
        while first:
            q.append(first.popleft())
            q.append(q.popleft())
        
        return q
