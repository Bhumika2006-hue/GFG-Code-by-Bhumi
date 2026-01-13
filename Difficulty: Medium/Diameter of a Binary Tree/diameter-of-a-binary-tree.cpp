/*
class Node {
public:
    int data;
    Node* left;
    Node* right;

    Node(int val) {
        data = val;
        left = NULL;
        right = NULL;
    }
};

Node* newNode(int val) {
    return new Node(val);
}
*/

class Solution {
  public:
  int height(Node* root,int &ans){
      //base case
      if(!root) return 0;
      //recursive case
      int LH=height(root->left,ans);
      int RH=height(root->right,ans);
      ans=max(ans,LH+RH);
      return max(LH,RH)+1;
  }
    int diameter(Node* root) {
        //Code with Radheshyam(.^.)
        int ans=0;
        height(root,ans);
        return ans;
    }
};