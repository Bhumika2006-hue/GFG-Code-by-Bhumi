class Solution:
    def countRevPairs(self, arr):
        return self.mergeSort(arr, 0, len(arr) - 1)

    def mergeSort(self, arr, low, high):
        if low >= high:
            return 0
        
        mid = (low + high) // 2
        count = self.mergeSort(arr, low, mid)
        count += self.mergeSort(arr, mid + 1, high)
        
        # Step 1: Count reverse pairs between the two sorted halves
        count += self.countPairs(arr, low, mid, high)
        
        # Step 2: Standard merge to sort the array
        self.merge(arr, low, mid, high)
        
        return count

    def countPairs(self, arr, low, mid, high):
        count = 0
        right = mid + 1
        for i in range(low, mid + 1):
            # While left element > 2 * right element, it's a reverse pair
            while right <= high and arr[i] > 2 * arr[right]:
                right += 1
            count += (right - (mid + 1))
        return count

    def merge(self, arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1
        
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1
        
        while left <= mid:
            temp.append(arr[left])
            left += 1
        while right <= high:
            temp.append(arr[right])
            right += 1
            
        for i in range(len(temp)):
            arr[low + i] = temp[i]