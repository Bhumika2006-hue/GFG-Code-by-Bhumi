class Solution:
    def countDistinct(self, arr, k):
        n = len(arr)
        result = []
        freq_map = {}
        
        # 1. Process the first window of size k
        for i in range(k):
            freq_map[arr[i]] = freq_map.get(arr[i], 0) + 1
            
        # Store the count of distinct elements in the first window
        result.append(len(freq_map))
        
        # 2. Slide the window from index k to n-1
        for i in range(k, n):
            # Element to remove: arr[i - k]
            out_elem = arr[i - k]
            freq_map[out_elem] -= 1
            
            # If frequency reaches 0, remove the key to maintain correct len()
            if freq_map[out_elem] == 0:
                del freq_map[out_elem]
                
            # Element to add: arr[i]
            in_elem = arr[i]
            freq_map[in_elem] = freq_map.get(in_elem, 0) + 1
            
            # The length of the map is the number of distinct elements
            result.append(len(freq_map))
            
        return result
        
        