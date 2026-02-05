class Solution:
    def maximumMeetings(self, start, end):
        meetings = sorted(zip(start, end), key=lambda x: x[1])
        
        count = 0
        last_end = -1
        
        for s, e in meetings:
            if s > last_end:
                count += 1
                last_end = e
        
        return count
