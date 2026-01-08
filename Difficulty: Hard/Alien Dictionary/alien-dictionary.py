from collections import deque, defaultdict

class Solution:
    def findOrder(self, words: list[str]) -> str:
        # 1. Map all unique characters to an in-degree of 0
        adj = defaultdict(set)
        in_degree = {char: 0 for word in words for char in word}
        
        # 2. Build the graph by comparing adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            min_len = min(len(w1), len(w2))
            
            # Edge Case: If a longer word is a prefix of a shorter word, it's invalid
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    # Only the first differing character defines the order
                    break
        
        # 3. Kahn's Algorithm (BFS Topological Sort)
        # Start with characters that have no dependencies (in-degree 0)
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        result = []
        
        while queue:
            curr = queue.popleft()
            result.append(curr)
            
            for neighbor in adj[curr]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 4. Final Validation
        # If result doesn't contain all unique characters, there is a cycle
        if len(result) < len(in_degree):
            return ""
            
        return "".join(result)