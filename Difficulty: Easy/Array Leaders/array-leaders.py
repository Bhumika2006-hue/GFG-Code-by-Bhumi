class Solution:
    def leaders(self, arr):
        n = len(arr)
        leaders = []
        
        max_right = arr[-1]
        leaders.append(max_right)

        for i in range(n - 2, -1, -1):
            if arr[i] >= max_right:
                max_right = arr[i]
                leaders.append(arr[i])

        return leaders[::-1]
