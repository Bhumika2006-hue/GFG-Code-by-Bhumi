class Solution:
    def insertAtEnd(self, head, x):
        new_node = Node(x)
        
        # If list is empty
        if head is None:
            return new_node
        
        curr = head
        while curr.next:
            curr = curr.next
        
        curr.next = new_node
        return head
