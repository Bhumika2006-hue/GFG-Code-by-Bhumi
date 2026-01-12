class Solution:
    def isPatternPresent(self, S, P):
        # Case 1: Start Anchor '^'
        if P.startswith('^'):
            # Extract pattern after '^'
            actual_pattern = P[1:]
            # Check if S starts with this pattern
            if S.startswith(actual_pattern):
                return 1
            else:
                return 0
        
        # Case 2: End Anchor '$'
        elif P.endswith('$'):
            # Extract pattern before '$'
            actual_pattern = P[:-1]
            # Check if S ends with this pattern
            if S.endswith(actual_pattern):
                return 1
            else:
                return 0
        
        # Case 3: Substring search (no anchors)
        else:
            if P in S:
                return 1
            else:
                return 0