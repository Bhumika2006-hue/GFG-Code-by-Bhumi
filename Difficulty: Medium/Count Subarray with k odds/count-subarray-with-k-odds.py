class Solution:
    def countSubarrays(self, arr, k):
        # Dictionary to store the frequency of prefix odd counts
        # Initialize with {0: 1} to handle cases where current_odds == k
        prefix_counts = {0: 1}
        
        current_odds = 0
        total_subarrays = 0
        
        for num in arr:
            # Check if the current number is odd
            if num % 2 != 0:
                current_odds += 1
            
            # If (current_odds - k) exists in our map, it means there are 
            # prefix_counts[current_odds - k] subarrays ending here with k odds
            if (current_odds - k) in prefix_counts:
                total_subarrays += prefix_counts[current_odds - k]
            
            # Update the map with the current prefix odd count
            prefix_counts[current_odds] = prefix_counts.get(current_odds, 0) + 1
            
        return total_subarrays
        