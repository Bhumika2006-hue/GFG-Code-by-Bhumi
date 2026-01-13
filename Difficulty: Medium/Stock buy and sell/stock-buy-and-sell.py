class Solution:
    # Function to find the maximum profit
    def stockBuySell(self, arr):
        profit = 0

        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                profit += arr[i] - arr[i - 1]

        return profit
