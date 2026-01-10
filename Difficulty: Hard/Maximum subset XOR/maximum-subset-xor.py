class Solution:
    def maxSubsetXOR(self, arr, N):
        index = 0  # Tracks the position in the array to place the pivot
        
        # Iterate from the Most Significant Bit (MSB) to the LSB
        for i in range(20, -1, -1):
            # Find a number with the i-th bit set
            max_element = -float('inf')
            max_idx = index
            
            for j in range(index, N):
                if (arr[j] & (1 << i)) != 0:
                    max_idx = j
                    break
            else:
                # No number has the i-th bit set, move to the next bit
                continue
                
            # Swap the found element with the element at the 'index' position
            arr[index], arr[max_idx] = arr[max_idx], arr[index]
            
            # Use the pivot element to clear the i-th bit from all other elements
            for j in range(N):
                if j != index and (arr[j] & (1 << i)) != 0:
                    arr[j] ^= arr[index]
            
            # Increment index to move to the next pivot position
            index += 1
            if index == N:
                break
                
        # The maximum XOR is simply the XOR sum of all elements in the basis
        res = 0
        for val in arr:
            res ^= val
            
        return res