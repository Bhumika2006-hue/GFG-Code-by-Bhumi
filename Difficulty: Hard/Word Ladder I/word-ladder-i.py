from collections import deque

class Solution:
    def wordLadderLength(self, startWord, targetWord, wordList):
        # Convert list to set for O(1) lookups
        word_set = set(wordList)
        
        # If targetWord isn't in the list, no transformation is possible
        if targetWord not in word_set:
            return 0
            
        # Queue for BFS: (current_word, current_length)
        queue = deque([(startWord, 1)])
        
        # To avoid visiting the same word again
        if startWord in word_set:
            word_set.remove(startWord)
            
        while queue:
            word, length = queue.popleft()
            
            # If we reached the target, return the length
            if word == targetWord:
                return length
            
            # Try changing every character of the current word
            for i in range(len(word)):
                original_char = word[i]
                
                # Replace character with 'a' through 'z'
                for c in range(ord('a'), ord('z') + 1):
                    char = chr(c)
                    if char == original_char:
                        continue
                    
                    new_word = word[:i] + char + word[i+1:]
                    
                    # If the new word is in our set, it's a valid next step
                    if new_word in word_set:
                        queue.append((new_word, length + 1))
                        # Remove from set to mark as visited
                        word_set.remove(new_word)
        
        return 0