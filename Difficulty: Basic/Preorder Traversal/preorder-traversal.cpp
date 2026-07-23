class Solution {
  private:
    void traverse(Node* root, vector<int>& result) {
        if (root == NULL) return;
        
        // 1. Visit Root
        result.push_back(root->data);
        
        // 2. Visit Left Subtree
        traverse(root->left, result);
        
        // 3. Visit Right Subtree
        traverse(root->right, result);
    }

  public:
    vector<int> preOrder(Node* root) {
        vector<int> result;
        traverse(root, result);
        return result;
    }
};