from collections import deque, defaultdict

class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        wordSet = set(wordList)
        if targetWord not in wordSet:
            return []
        
        # BFS to find the shortest distance to each reachable word
        distance_map = {startWord: 0}
        queue = deque([startWord])
        
        while queue:
            word = queue.popleft()
            if word == targetWord:
                break
                
            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + char + word[i+1:]
                    if new_word in wordSet and new_word not in distance_map:
                        distance_map[new_word] = distance_map[word] + 1
                        queue.append(new_word)
        
        # If targetWord was never reached
        if targetWord not in distance_map:
            return []
            
        results = []
        
        # Backtracking (DFS) to find all paths from targetWord back to startWord
        def backtrack(current_word, path):
            if current_word == startWord:
                results.append(path[::-1]) # Reverse to get start -> target
                return
            
            curr_dist = distance_map[current_word]
            for i in range(len(current_word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    prev_word = current_word[:i] + char + current_word[i+1:]
                    # Only move to words that are exactly one step closer to startWord
                    if prev_word in distance_map and distance_map[prev_word] == curr_dist - 1:
                        backtrack(prev_word, path + [prev_word])

        backtrack(targetWord, [targetWord])
        return results