class Solution {
public:
    struct Node {
        char data;
        int freq;
        Node* left;
        Node* right;
        Node(char d, int f) : data(d), freq(f), left(NULL), right(NULL) {}
        Node(int f, Node* l, Node* r) : data('\0'), freq(f), left(l), right(r) {}
    };
    
    struct Compare {
        bool operator()(Node* a, Node* b) {
            return a->freq > b->freq;  // Min heap
        }
    };
    
    void preorder(Node* root, string code, vector<string>& codes) {
        if (!root) return;
        
        // Leaf node - store code
        if (!root->left && !root->right) {
            codes.push_back(code);
            return;
        }
        
        // Preorder: root, left, right
        preorder(root->left, code + "0", codes);
        preorder(root->right, code + "1", codes);
    }
    
    vector<string> huffmanCodes(string S, vector<int> f, int N) {
        priority_queue<Node*, vector<Node*>, Compare> pq;
        
        // Create leaf nodes
        for (int i = 0; i < N; i++) {
            pq.push(new Node(S[i], f[i]));
        }
        
        // Build Huffman tree
        while (pq.size() > 1) {
            Node* left = pq.top(); pq.pop();
            Node* right = pq.top(); pq.pop();
            
            // New internal node (freq sum, left, right)
            Node* parent = new Node(left->freq + right->freq, left, right);
            pq.push(parent);
        }
        
        // Root of Huffman tree
        Node* root = pq.top();
        
        // Get codes in preorder traversal
        vector<string> codes;
        preorder(root, "", codes);
        
        return codes;
    }
};
