
/*  Node is defined as
  struct Node {
    int data;
    struct Node *next;
    Node(int x) {
        data = x;
        next = NULL;
    }
};*/
class Solution {
  public:
    Node* segregate(Node* head) {
        int zeros=0,ones=0,twos=0;
        Node *temp=head;
        while(temp){
            if(temp->data==0)zeros++;
            else if(temp->data==1)ones++;
            else twos++;
            temp=temp->next;
        }
        temp=head;
        while(zeros){
            temp->data=0;
            zeros--;
            temp=temp->next;
        }
        while(ones){
            temp->data=1;
            ones--;
            temp=temp->next;
        }
        while(twos){
            temp->data=2;
            twos--;
            temp=temp->next;
        }
        return head;
    }
};
