class Solution:
    def find(self, arr, x):
        def first_occurrence():
            low, high = 0, len(arr) - 1
            res = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == x:
                    res = mid
                    high = mid - 1
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return res

        def last_occurrence():
            low, high = 0, len(arr) - 1
            res = -1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == x:
                    res = mid
                    low = mid + 1
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return res

        return [first_occurrence(), last_occurrence()]
