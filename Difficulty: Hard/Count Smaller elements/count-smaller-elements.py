class Solution:
    def constructLowerArray(self, arr):
        n = len(arr)
        result = [0] * n
        # We store pairs of (value, original_index) to track counts
        items = [[val, i] for i, val in enumerate(arr)]
        
        def merge_sort(indices):
            if len(indices) <= 1:
                return indices
            
            mid = len(indices) // 2
            left = merge_sort(indices[:mid])
            right = merge_sort(indices[mid:])
            
            return merge(left, right)
            
        def merge(left, right):
            merged = []
            i = j = 0
            right_count = 0 # Count of elements from 'right' smaller than current 'left'
            
            while i < len(left) and j < len(right):
                if right[j][0] < left[i][0]:
                    # Element in right is smaller, it "jumps" over left elements
                    merged.append(right[j])
                    right_count += 1
                    j += 1
                else:
                    # Element in left is smaller or equal
                    # Add the number of right elements that were smaller than it
                    result[left[i][1]] += right_count
                    merged.append(left[i])
                    i += 1
            
            # Process remaining elements
            while i < len(left):
                result[left[i][1]] += right_count
                merged.append(left[i])
                i += 1
            while j < len(right):
                merged.append(right[j])
                j += 1
                
            return merged

        merge_sort(items)
        return result