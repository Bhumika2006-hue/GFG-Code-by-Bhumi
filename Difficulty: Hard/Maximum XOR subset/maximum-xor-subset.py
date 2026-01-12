# User function Template for python3

class Solution:
    def maxXor(self, a, n):
        # Since max value is 10^5, 20 bits are sufficient (2^19 > 10^5)
        # basis[i] will store a number whose highest set bit is at index i
        basis = [0] * 20
        
        for x in a:
            for i in range(19, -1, -1):
                # Check if the i-th bit is set in x
                if not (x & (1 << i)):
                    continue
                
                if not basis[i]:
                    # If no basis element exists for this bit, insert x
                    basis[i] = x
                    break
                
                # If a basis element exists, XOR x with it to reduce x
                x ^= basis[i]
        
        # Initialize result
        res = 0
        
        # Greedily build the maximum XOR value
        for i in range(19, -1, -1):
            # If XORing with the basis element at this bit increases res, do it
            if (res ^ basis[i]) > res:
                res ^= basis[i]
                
        return res