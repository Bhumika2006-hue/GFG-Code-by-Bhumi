class Solution:
    def kBitFlips(self, arr, k):
        n = len(arr)
        total_flips = 0
        current_window_flips = 0
        
        for i in range(n):
            # 1. Check if a flip that started k positions ago has ended
            if i >= k and arr[i - k] == 2:
                current_window_flips -= 1
            
            # 2. Determine if the current element needs to be flipped
            # (current_window_flips % 2) tells us if the bit is currently inverted
            # If current bit is 0 and flips are even, it's still 0.
            # If current bit is 1 and flips are odd, it's now 0.
            if current_window_flips % 2 == arr[i]:
                # If there's not enough room to flip a subarray of length k
                if i + k > n:
                    return -1
                
                # Perform flip
                total_flips += 1
                current_window_flips += 1
                # Mark this index as the start of a flip using a special value
                arr[i] = 2
        
        return total_flips