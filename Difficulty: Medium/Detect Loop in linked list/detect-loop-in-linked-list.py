class Solution:
    # Function to check if the linked list has a loop.
    def detectLoop(self, head):
        # Handle empty list or single node without a loop
        if not head or not head.next:
            return False
        
        # Initialize two pointers
        slow = head
        fast = head
        
        # Traverse the list
        while fast and fast.next:
            slow = slow.next          # Move slow by 1 step
            fast = fast.next.next     # Move fast by 2 steps
            
            # If they meet, there is a loop
            if slow == fast:
                return True
        
        # If we reach the end of the list, no loop exists
        return False