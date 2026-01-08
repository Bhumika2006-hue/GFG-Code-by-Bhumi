class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

class Solution:
    def cloneLinkedList(self, head):
        if not head:
            return None
        
        # Step 1: Create duplicate nodes and interweave them
        # Original: A -> B -> C
        # Interweaved: A -> A' -> B -> B' -> C -> C'
        curr = head
        while curr:
            copy = Node(curr.data)
            copy.next = curr.next
            curr.next = copy
            curr = copy.next
            
        
            
        # Step 2: Set the random pointers for the copied nodes
        curr = head
        while curr:
            if curr.random:
                # The copy of curr's random node is sitting right after the original random node
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        
            
        # Step 3: Separate the interweaved list into two original lists
        curr = head
        clone_head = head.next
        copy_curr = clone_head
        
        while curr:
            curr.next = curr.next.next
            if copy_curr.next:
                copy_curr.next = copy_curr.next.next
            
            curr = curr.next
            copy_curr = copy_curr.next
            
        return clone_head