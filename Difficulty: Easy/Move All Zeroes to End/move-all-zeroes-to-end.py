class Solution:
    def pushZerosToEnd(self, arr):
        pos = 0
        
        # Move non-zero elements forward
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[pos] = arr[i]
                pos += 1
        
        # Fill the rest with zeros
        while pos < len(arr):
            arr[pos] = 0
            pos += 1
