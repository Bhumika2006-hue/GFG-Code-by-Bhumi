class TrieNode
    {
      public:
        // pointer array for 26 letters
        vector<TrieNode *> children;
 
        // indices of palindromic words
        vector<int> indices;
 
        // index of word in array
        int idx;
 
        TrieNode() : idx(-1)
        {
 
            // initialize children array to NULL
            children.resize(26, nullptr);
        }
    };

class Solution {
  public:
  
    bool isPalindrome(string str, int i, int j)
    {
 
        // compare each character from starting
        // with its corresponding character from last
        while (i < j)
        {
            if (str[i] != str[j])
                return false;
            i++, j--;
        }
        return true;
    }
 
        // If not present, inserts reverse of word into Trie. If
        // the word is prefix of a Trie node, just mark leaf node
        void insert(TrieNode *root, string word, int idx)
        {
            TrieNode *node = root;
 
            // Start traversing word from the last
            for (int i = word.length() - 1; i >= 0; i--)
            {
                // If current word is palindrome till this
                // i, store index of current word.
                if (isPalindrome(word, 0, i))
                    (node->indices).push_back(idx);
 
                // If it is not available in Trie
                // then store it
                int index = word[i] - 'a';
                if (!node->children[index])
                    node->children[index] = new TrieNode();
 
                // move to new TrieNode
                node = node->children[index];
            }
            node->idx = idx;
            node->indices.push_back(idx);
        }
 
        // Returns true if word presents in Trie, else false
        bool search(TrieNode *root, string word, int idx)
        {
            TrieNode *node = root;
            for (int i = 0; i < word.length() && node; i++)
            {
                int index = word[i] - 'a';
 
                // If it is present also check upto
                // which index it is palindrome
                if (node->idx >= 0 && node->idx != idx && isPalindrome(word, i, word.size() - 1))
                    return true;
 
                node = node->children[index];
            }
 
            if (node)
            {
                for (int i : node->indices)
                {
                    if (idx != i)
                        return true;
                }
            }
 
            return false;
        }
 
        // Function to check if a palindrome pair exists
        bool palindromePair(vector<string> &arr)
        {
 
            // Construct trie
            TrieNode *root = new TrieNode();
            for (int i = 0; i < arr.size(); i++)
                insert(root, arr[i], i);
 
            // Search for different keys
            for (int i = 0; i < arr.size(); i++)
            {
                if (search(root, arr[i], i))
                    return true;
            }
            return false;
        }
 
};