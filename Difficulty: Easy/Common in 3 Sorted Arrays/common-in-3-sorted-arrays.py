class Solution:
    def commonElements(self, arr1, arr2, arr3):
        i = j = k = 0
        res = []

        n1, n2, n3 = len(arr1), len(arr2), len(arr3)

        while i < n1 and j < n2 and k < n3:
            if arr1[i] == arr2[j] == arr3[k]:
                # Avoid duplicates
                if not res or res[-1] != arr1[i]:
                    res.append(arr1[i])
                i += 1
                j += 1
                k += 1
            else:
                mn = min(arr1[i], arr2[j], arr3[k])
                if arr1[i] == mn:
                    i += 1
                elif arr2[j] == mn:
                    j += 1
                else:
                    k += 1

        return res if res else [-1]
