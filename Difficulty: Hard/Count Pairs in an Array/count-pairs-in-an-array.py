class Solution:
    def countPairs(self, arr, n):
        # Step 1: Transform the array to B[i] = i * arr[i]
        B = [i * arr[i] for i in range(n)]
        
        # Step 2: Use Merge Sort logic to count inversions
        return self.mergeSortAndCount(B, 0, n - 1)

    def mergeSortAndCount(self, arr, l, r):
        count = 0
        if l < r:
            mid = (l + r) // 2
            
            # Count inversions in left half, right half, and during merge
            count += self.mergeSortAndCount(arr, l, mid)
            count += self.mergeSortAndCount(arr, mid + 1, r)
            count += self.mergeAndCount(arr, l, mid, r)
            
        return count

    def mergeAndCount(self, arr, l, mid, r):
        left = arr[l : mid + 1]
        right = arr[mid + 1 : r + 1]
        
        i = j = 0
        k = l
        swaps = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                # If left[i] > right[j], then all elements to the right 
                # of left[i] are also greater than right[j]
                arr[k] = right[j]
                j += 1
                swaps += (len(left) - i)
            k += 1
            
        # Append remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            
        return swaps