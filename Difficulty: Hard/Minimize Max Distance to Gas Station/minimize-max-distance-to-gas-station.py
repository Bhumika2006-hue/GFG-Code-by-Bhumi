class Solution:
    def minMaxDist(self, stations, k):
        n = len(stations)
        
        # Helper function to check if a max distance 'dist' is achievable with k stations
        def isPossible(dist):
            required_stations = 0
            for i in range(n - 1):
                gap = stations[i+1] - stations[i]
                # If gap is 10 and dist is 3, we need 3 stations 
                # to create 4 segments of 2.5 each.
                required_stations += int(gap / dist)
            return required_stations <= k

        # Binary search range
        low = 0.0
        high = stations[-1] - stations[0]
        
        # Perform 100 iterations for high precision
        for _ in range(100):
            mid = (low + high) / 2
            if isPossible(mid):
                high = mid  # Try to find an even smaller maximum distance
            else:
                low = mid   # Distance is too small, need to increase it
                
        return round(high, 6)