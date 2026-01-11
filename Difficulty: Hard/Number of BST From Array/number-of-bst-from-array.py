class Solution:
    def countBSTs(self, arr):
        # Catalan numbers for n = 0 to 6
        # C0=1, C1=1, C2=2, C3=5, C4=14, C5=42, C6=132
        catalan = [1, 1, 2, 5, 14, 42, 132]
        
        n = len(arr)
        results = []
        
        # Sort the array to easily count elements smaller and larger than root
        sorted_arr = sorted(arr)
        
        for root_val in arr:
            # Find how many elements are smaller than root_val
            # and how many are larger.
            smaller_count = 0
            for x in arr:
                if x < root_val:
                    smaller_count += 1
            
            larger_count = n - 1 - smaller_count
            
            # Use Catalan numbers to find combinations for left and right subtrees
            num_bsts = catalan[smaller_count] * catalan[larger_count]
            results.append(num_bsts)
            
        return results