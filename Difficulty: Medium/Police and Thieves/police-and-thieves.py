class Solution:
    def catchThieves(self, arr, k):
        police = []
        thieves = []

        # Store positions
        for i in range(len(arr)):
            if arr[i] == 'P':
                police.append(i)
            else:
                thieves.append(i)

        i = j = 0
        caught = 0

        # Two pointer matching
        while i < len(police) and j < len(thieves):
            if abs(police[i] - thieves[j]) <= k:
                caught += 1
                i += 1
                j += 1
            elif thieves[j] < police[i]:
                j += 1
            else:
                i += 1

        return caught
