class Solution:
    def overlapInt(self, arr):
        # Step 1: Extract all start times and end times
        starts = sorted([i[0] for i in arr])
        ends = sorted([i[1] for i in arr])
        
        n = len(arr)
        max_overlaps = 0
        current_overlaps = 0
        
        i = 0  # Pointer for starts
        j = 0  # Pointer for ends
        
        # Step 2: Use two pointers to sweep through the timeline
        while i < n:
            # If the next start is less than or equal to the next end,
            # it means a new interval has started before the previous one finished.
            # We use <= because the intervals are inclusive.
            if starts[i] <= ends[j]:
                current_overlaps += 1
                max_overlaps = max(max_overlaps, current_overlaps)
                i += 1
            else:
                # An interval has ended
                current_overlaps -= 1
                j += 1
                
        return max_overlaps