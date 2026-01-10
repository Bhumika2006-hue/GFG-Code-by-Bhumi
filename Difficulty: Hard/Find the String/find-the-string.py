class Solution:
    def findString(self, N, K):
        # Total number of unique substrings of length N is K^N
        # The total length of the resulting string should be K^N + N - 1
        
        seen = set()
        starting_node = "0" * (N - 1)
        res = []
        
        def dfs(curr_node):
            for i in range(K):
                # Form the potential substring (edge)
                edge = curr_node + str(i)
                if edge not in seen:
                    seen.add(edge)
                    # Move to the next node (suffix of length N-1)
                    dfs(edge[1:])
                    # Post-order addition is key for Eulerian circuits
                    res.append(str(i))
        
        dfs(starting_node)
        
        # Result is the starting prefix + the sequence of characters found
        return starting_node + "".join(res[::-1])