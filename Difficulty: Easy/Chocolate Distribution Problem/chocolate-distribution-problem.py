class Solution:
    def findMinDiff(self, arr, M):
        if M == 0 or M > len(arr):
            return 0
        
        arr.sort()
        n = len(arr)
        
        min_diff = float('inf')
        
        for i in range(n - M + 1):
            min_diff = min(min_diff, arr[i + M - 1] - arr[i])
        
        return min_diff
