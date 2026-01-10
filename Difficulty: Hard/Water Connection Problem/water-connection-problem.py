class Solution:
    def solve(self, n, p, a, b, d):
        # outgoing_to[i] stores which house house 'i' points to
        outgoing_to = [0] * (n + 1)
        # diameter_to[i] stores the diameter of the pipe leaving house 'i'
        diameter_to = [0] * (n + 1)
        # has_incoming[i] tracks if anyone points to house 'i'
        has_incoming = [False] * (n + 1)
        
        for i in range(p):
            u, v, weight = a[i], b[i], d[i]
            outgoing_to[u] = v
            diameter_to[u] = weight
            has_incoming[v] = True
            
        res = []
        
        # Iterate through all houses to find starting points (tanks)
        for i in range(1, n + 1):
            # A tank is installed if a house has an outgoing pipe but no incoming pipe
            if not has_incoming[i] and outgoing_to[i] != 0:
                tank = i
                min_dia = diameter_to[i]
                curr = outgoing_to[i]
                
                # Traverse the chain until we find a house with no outgoing pipe (tap)
                while outgoing_to[curr] != 0:
                    min_dia = min(min_dia, diameter_to[curr])
                    curr = outgoing_to[curr]
                
                tap = curr
                res.append([tank, tap, min_dia])
        
        # Result must be sorted by house number of the tank
        res.sort()
        return res