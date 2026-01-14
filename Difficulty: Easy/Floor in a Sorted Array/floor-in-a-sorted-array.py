class Solution:
    def findFloor(self, arr, x):
        low, high = 0, len(arr) - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] <= x:
                ans = mid          # possible floor
                low = mid + 1      # move right to find last occurrence
            else:
                high = mid - 1

        return ans
