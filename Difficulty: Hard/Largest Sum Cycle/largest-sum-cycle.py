import sys

# Increase recursion depth for deep graphs
sys.setrecursionlimit(10**6)

class Solution():
    def largestSumCycle(self, N, Edge):
        vis = [False] * N
        path_vis = [False] * N
        max_cycle_sum = -1
        
        # We use this to track the sequence of nodes in the current path
        # to easily calculate the sum once a cycle is found.
        path_stack = []

        for i in range(N):
            if not vis[i]:
                curr = i
                local_path = []
                while curr != -1 and not vis[curr]:
                    vis[curr] = True
                    path_vis[curr] = True
                    local_path.append(curr)
                    curr = Edge[curr]
                
                # If we hit a node that is in path_vis, we found a cycle
                if curr != -1 and path_vis[curr]:
                    curr_sum = 0
                    # Traverse backwards through local_path to find where the cycle starts
                    for j in range(len(local_path) - 1, -1, -1):
                        curr_sum += local_path[j]
                        if local_path[j] == curr:
                            break
                    max_cycle_sum = max(max_cycle_sum, curr_sum)
                
                # Clean up path_vis for the next component
                for node in local_path:
                    path_vis[node] = False
                    
        return max_cycle_sum