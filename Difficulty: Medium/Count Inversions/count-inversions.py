class Solution:
    def inversionCount(self, arr):
        n = len(arr)
        # Temporary array for merge process
        temp_arr = [0] * n
        return self._merge_sort(arr, temp_arr, 0, n - 1)

    def _merge_sort(self, arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            # Find the midpoint
            mid = (left + right) // 2

            # Count inversions in left half
            inv_count += self._merge_sort(arr, temp_arr, left, mid)

            # Count inversions in right half
            inv_count += self._merge_sort(arr, temp_arr, mid + 1, right)

            # Count merge inversions
            inv_count += self._merge(arr, temp_arr, left, mid, right)
            
        return inv_count

    def _merge(self, arr, temp_arr, left, mid, right):
        i = left    # Starting index for left subarray
        j = mid + 1 # Starting index for right subarray
        k = left    # Starting index to be sorted
        inv_count = 0

        # While there are elements in both subarrays
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                # Inversion occurs because arr[i] > arr[j]
                # All elements from current i to mid in left subarray are inversions
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)
                j += 1
            k += 1

        # Copy remaining elements of left subarray, if any
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1

        # Copy remaining elements of right subarray, if any
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        # Copy back to original array
        for loop_var in range(left, right + 1):
            arr[loop_var] = temp_arr[loop_var]

        return inv_count