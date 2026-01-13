/*

struct Node {
    int data;
    struct Node *next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};

*/

class Solution {
  public:
    Node* rotate(Node* head, int k) {
        //Code with Radheshyam (.^.)
        if(k==0 || head == NULL) return head;
        int length=1;
        Node* temp=head;
        
        while(temp->next!=NULL){
            temp=temp->next;
            length+=1;
        }
        k=k%length;
        if(k==0) return head;
       
       temp->next= head;
       temp=head;
       
      for(int i=1;i<k;i++){
       temp=temp->next;
       }
    
    Node* newHead=temp->next;
    temp->next=NULL;
    return newHead;
    }
};