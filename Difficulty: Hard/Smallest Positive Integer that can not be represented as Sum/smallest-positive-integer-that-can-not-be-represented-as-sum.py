class Solution:
    def smallestpositive(self, array, n): 
        # 1. Sort the array to process elements greedily
        # Time complexity of sorting: O(N log N)
        array.sort()
        
        # 2. 'res' is the smallest positive integer we are trying to form
        res = 1
        
        # 3. Iterate through the sorted elements
        for x in array:
            # If the current element is <= res, we can form all 
            # values up to (res + x - 1).
            # So the new smallest unformable value is res + x.
            if x <= res:
                res += x
            else:
                # If x > res, we found a gap. 'res' cannot be formed.
                break
                
        return res