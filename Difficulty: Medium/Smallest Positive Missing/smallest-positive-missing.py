class Solution:
    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        n = len(arr)
        
        # Step 1: Place each number in its correct position if possible
        for i in range(n):
            # While the current number is in range [1, n] and 
            # not at its correct position (arr[i]-1), swap it.
            # We also check arr[i] != arr[arr[i]-1] to avoid infinite loops with duplicates.
            while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
                # Correct index for arr[i] is arr[i] - 1
                correct_idx = arr[i] - 1
                arr[i], arr[correct_idx] = arr[correct_idx], arr[i]
        
        # Step 2: Find the first index that doesn't have the correct number
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1
        
        # Step 3: If all positions [1, n] are filled, the missing number is n + 1
        return n + 1