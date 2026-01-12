class Solution:
    def sumOfMax(self, arr):
        n = len(arr)
        if n == 0:
            return 0
        
        # left[i] = number of elements to the left of i smaller than arr[i]
        left = [0] * n
        # right[i] = number of elements to the right of i smaller than or equal to arr[i]
        right = [0] * n
        
        stack = []
        
        # Find nearest greater element to the left
        for i in range(n):
            count = 1
            while stack and stack[-1][0] < arr[i]:
                count += stack.pop()[1]
            stack.append((arr[i], count))
            left[i] = count
            
        stack = []
        
        # Find nearest greater element to the right
        # Use <= here to handle duplicate elements correctly
        for i in range(n - 1, -1, -1):
            count = 1
            while stack and stack[-1][0] <= arr[i]:
                count += stack.pop()[1]
            stack.append((arr[i], count))
            right[i] = count
            
        total_sum = 0
        for i in range(n):
            # Element arr[i] is the maximum in (left[i] * right[i]) subarrays
            total_sum += arr[i] * left[i] * right[i]
            
        return total_sum