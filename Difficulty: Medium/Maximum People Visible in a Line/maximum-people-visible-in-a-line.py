class Solution:
    def maxPeople(self, arr):
        n = len(arr)
        if n == 0: return 0
        
        # left[i] will store the index of the nearest element to the left 
        # that is >= arr[i]. If none, -1.
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)
            
        # right[i] will store the index of the nearest element to the right
        # that is >= arr[i]. If none, n.
        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
            
        # The number of people person i sees is (right[i] - 1) - (left[i] + 1) + 1
        # which simplifies to: right[i] - left[i] - 1
        max_visible = 0
        for i in range(n):
            # The count includes self, plus everyone between left[i] and right[i]
            current_count = right[i] - left[i] - 1
            if current_count > max_visible:
                max_visible = current_count
                
        return max_visible