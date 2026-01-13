class Solution:
    def findTriplets(self, arr):
        n = len(arr)
        arr.sort()

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                curr_sum = arr[i] + arr[left] + arr[right]

                if curr_sum == 0:
                    return True
                elif curr_sum < 0:
                    left += 1
                else:
                    right -= 1

        return False
