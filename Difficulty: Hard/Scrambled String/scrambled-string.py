class Solution:
    def __init__(self):
        self.memo = {}

    def isScramble(self, S1: str, S2: str) -> bool:
        # If the result for this pair of strings is already computed
        state = S1 + "_" + S2
        if state in self.memo:
            return self.memo[state]

        # Base Cases
        if S1 == S2:
            self.memo[state] = True
            return True
        
        if len(S1) != len(S2) or sorted(S1) != sorted(S2):
            self.memo[state] = False
            return False

        n = len(S1)
        # Try splitting the strings at every possible position i
        for i in range(1, n):
            # Case 1: No swap at this node
            # S1: [0:i][i:n]  vs  S2: [0:i][i:n]
            if (self.isScramble(S1[:i], S2[:i]) and 
                self.isScramble(S1[i:], S2[i:])):
                self.memo[state] = True
                return True

            # Case 2: Swapped children at this node
            # S1: [0:i][i:n]  vs  S2: [n-i:n][0:n-i]
            if (self.isScramble(S1[:i], S2[n-i:]) and 
                self.isScramble(S1[i:], S2[:n-i])):
                self.memo[state] = True
                return True

        self.memo[state] = False
        return False