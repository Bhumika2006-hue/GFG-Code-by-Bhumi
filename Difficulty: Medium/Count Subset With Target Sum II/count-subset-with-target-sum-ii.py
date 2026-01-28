class Solution:
    def countSubset(self, arr, k):
        n = len(arr)
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
        
        # Generate subset sums recursively (faster than bitmask in Python)
        def gen(nums):
            sums = []
            def dfs(i, s):
                if i == len(nums):
                    sums.append(s)
                    return
                dfs(i+1, s)
                dfs(i+1, s + nums[i])
            dfs(0, 0)
            return sums
        
        L = gen(left)
        R = gen(right)
        
        L.sort()
        R.sort()
        
        # Two pointer count pairs sum == k
        i, j = 0, len(R) - 1
        ans = 0
        
        while i < len(L) and j >= 0:
            s = L[i] + R[j]
            if s == k:
                # count duplicates
                c1, c2 = 1, 1
                while i+1 < len(L) and L[i] == L[i+1]:
                    i += 1
                    c1 += 1
                while j-1 >= 0 and R[j] == R[j-1]:
                    j -= 1
                    c2 += 1
                ans += c1 * c2
                i += 1
                j -= 1
            elif s < k:
                i += 1
            else:
                j -= 1
        
        return ans
