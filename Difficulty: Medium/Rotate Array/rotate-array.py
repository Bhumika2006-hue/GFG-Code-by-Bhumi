#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n = len(arr)
        
        # 1. Handle cases where d is greater than array size
        d = d % n
        
        # 2. Define a helper function to reverse elements in place
        def reverse(start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        
        # 3. Apply the three-step reversal
        # Reverse the first d elements: [0...d-1]
        reverse(0, d - 1)
        
        # Reverse the remaining elements: [d...n-1]
        reverse(d, n - 1)
        
        # Reverse the whole array: [0...n-1]
        reverse(0, n - 1)