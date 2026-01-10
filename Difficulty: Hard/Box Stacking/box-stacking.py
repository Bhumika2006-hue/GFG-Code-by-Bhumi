class Solution:
    def maxHeight(self, height, width, length):
        n = len(height)
        orientations = []

        # Step 1: Generate all 3 orientations for each box
        for i in range(n):
            h, w, l = height[i], width[i], length[i]
            
            # Orientation 1: h is height
            orientations.append((max(w, l), min(w, l), h))
            # Orientation 2: w is height
            orientations.append((max(h, l), min(h, l), w))
            # Orientation 3: l is height
            orientations.append((max(h, w), min(h, w), l))

        # Step 2: Sort by base area in descending order
        # This simplifies the problem to a Longest Increasing Subsequence variation
        orientations.sort(key=lambda x: x[0] * x[1], reverse=True)

        num_variants = len(orientations)
        dp = [0] * num_variants

        # Step 3: Compute DP (LIS variant)
        for i in range(num_variants):
            # Base height for the current orientation
            dp[i] = orientations[i][2]
            
            # Check all previous boxes to see if orientations[i] can sit on top
            for j in range(i):
                # Condition: lower box (j) must have strictly larger L and W than upper box (i)
                if orientations[i][0] < orientations[j][0] and \
                   orientations[i][1] < orientations[j][1]:
                    dp[i] = max(dp[i], dp[j] + orientations[i][2])

        return max(dp)