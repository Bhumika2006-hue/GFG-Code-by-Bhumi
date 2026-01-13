/*
class Node {
 public:
    int data;
    Node *next;

    Node(int x) {
        data = x;
        next = NULL;
    }
};
*/

class Solution {
  public:
  int findLength(Node *slow, Node *fast){
      int count = 1;
      fast=fast->next;
      while(fast!=slow){
          count++;
          fast=fast->next;
      }
      return count;
  }
  
    int lengthOfLoop(Node *head) {
        // Code with Radheshyam (.^.)
        Node *slow = head, *fast = head;
        
        while(fast!=NULL && fast->next != NULL){
            slow=slow->next;
            fast=fast->next->next;
            if(slow==fast) return findLength(slow,fast);
        }
        return 0;
    }
};