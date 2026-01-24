class Solution:
    def josephus(self, n, k):
        res = 0  # 0-based result
        for i in range(1, n + 1):
            res = (res + k) % i
        return res + 1  # convert to 1-based
