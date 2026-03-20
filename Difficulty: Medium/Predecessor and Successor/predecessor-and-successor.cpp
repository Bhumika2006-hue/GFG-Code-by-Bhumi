
/* BST Node
class Node
{
   public:
    int data;
    Node *left;
    Node *right;

    Node(int x){
        data = x;
        left = NULL;
        right = NULL;
    }
}; */

class Solution {
  public:
        Node* rightMost(Node* node){
            while(node->right) node = node->right;
            return node;
        }
        
        Node* leftMost(Node* node){
            while(node->left) node = node->left;
            return node;
        }
  
    vector<Node*> findPreSuc(Node* root, int key) {
        // Code with Radheshyam (.^.)
        Node* pre=NULL;
        Node* curr=root;
        Node* suc=NULL;
        
        while(curr){
            if(curr->data < key){
            
            pre = curr;
            curr=curr->right;
            
          } else if(curr->data > key){
            
            suc = curr;
            curr=curr->left;
            
            } else{
            
            if(curr->left) pre = rightMost(curr->left);
            
            if(curr->right) suc = leftMost(curr->right);
            break;
            }
        }
            return {pre,suc};
    }
};

