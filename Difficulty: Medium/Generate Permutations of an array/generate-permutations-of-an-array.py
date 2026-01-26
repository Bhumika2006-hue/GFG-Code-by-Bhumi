class Solution:
    def permuteDist(self, arr):
        res = []
        
        def backtrack(i):
            if i == len(arr):
                res.append(arr[:])
                return
            
            for j in range(i, len(arr)):
                arr[i], arr[j] = arr[j], arr[i]   # swap
                backtrack(i + 1)
                arr[i], arr[j] = arr[j], arr[i]   # backtrack
        
        backtrack(0)
        return res
