class Solution:
    # Function to remove a loop in the linked list.
    def removeLoop(self, head):
        if not head or not head.next:
            return
        
        slow = head
        fast = head
        
        # 1. Detect if a loop exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                self.breakLoop(head, slow)
                return

    def breakLoop(self, head, meeting_point):
        ptr1 = head
        ptr2 = meeting_point
        
        # Special Case: If the loop starts at the head
        if ptr1 == ptr2:
            # Find the last node of the loop
            while ptr2.next != ptr1:
                ptr2 = ptr2.next
            ptr2.next = None
            return

        # 2. Find the start of the loop
        # Move both pointers at the same speed
        while ptr1.next != ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        # 3. Break the connection
        # ptr2 is now the last node in the cycle
        ptr2.next = None