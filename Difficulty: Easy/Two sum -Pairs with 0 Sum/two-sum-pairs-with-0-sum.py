class Solution:
    def getPairs(self, arr):
        arr.sort()
        res = []
        left, right = 0, len(arr) - 1

        while left < right:
            s = arr[left] + arr[right]

            if s == 0:
                res.append([arr[left], arr[right]])

                # Skip duplicates
                l_val = arr[left]
                r_val = arr[right]
                while left < right and arr[left] == l_val:
                    left += 1
                while left < right and arr[right] == r_val:
                    right -= 1

            elif s < 0:
                left += 1
            else:
                right -= 1

        return res
