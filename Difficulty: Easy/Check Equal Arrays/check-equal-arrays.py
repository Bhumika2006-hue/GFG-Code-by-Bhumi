from collections import Counter

class Solution:
    def checkEqual(self, a, b) -> bool:
        return Counter(a) == Counter(b)
