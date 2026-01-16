class Solution:
    def minMen(self, arr):
        n = len(arr)
        intervals = []

        # Build intervals
        for i in range(n):
            if arr[i] != -1:
                start = max(0, i - arr[i])
                end = min(n - 1, i + arr[i])
                intervals.append((start, end))

        intervals.sort()

        count = 0
        curr_end = 0
        i = 0
        max_reach = 0

        while curr_end < n:
            progressed = False

            while i < len(intervals) and intervals[i][0] <= curr_end:
                max_reach = max(max_reach, intervals[i][1])
                i += 1
                progressed = True

            if not progressed:
                return -1

            count += 1
            curr_end = max_reach + 1

        return count
