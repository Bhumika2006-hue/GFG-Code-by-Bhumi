class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)
        if n < k:
            return 0
            
        current_xor = 0
        
        # 1. Initial window XOR
        for i in range(k):
            current_xor ^= arr[i]
            
        max_xor = current_xor
        
        # 2. Slide the window
        for i in range(k, n):
            # XORing with arr[i-k] removes it from the window
            # XORing with arr[i] adds it to the window
            current_xor = current_xor ^ arr[i] ^ arr[i-k]
            
            if current_xor > max_xor:
                max_xor = current_xor
                
        return max_xor
        
       