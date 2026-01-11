import bisect

class Solution:
    def minInsAndDel(self, A, B, N, M):
        # Step 1: Create a mapping of elements in B to their indices
        # Since B has distinct elements, this is a 1-to-1 mapping
        b_map = {val: i for i, val in enumerate(B)}
        
        # Step 2: Filter A to include only elements present in B
        # Replace those elements with their indices in B
        target_indices = []
        for x in A:
            if x in b_map:
                target_indices.append(b_map[x])
        
        # Step 3: Find the Longest Increasing Subsequence (LIS) of target_indices
        # This LIS represents the length of the LCS of A and B
        lis = []
        for x in target_indices:
            # Find the position where x would be inserted in a sorted list
            idx = bisect.bisect_left(lis, x)
            if idx == len(lis):
                lis.append(x)
            else:
                lis[idx] = x
        
        lcs_length = len(lis)
        
        # Step 4: Total operations = (Deletions: N - L) + (Insertions: M - L)
        return N + M - 2 * lcs_length