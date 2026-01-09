class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return head

        # Step 1: Find the middle of the linked list
        # After this, 'slow' will be at the end of the first half
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        # Current list: 1 -> 2 -> 3 -> 4 -> 5, slow is at 3
        # We want to reverse: 4 -> 5 to 5 -> 4
        prev = None
        curr = slow.next
        slow.next = None # Break the link between first and second half
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # 'prev' is now the head of the reversed second half
        second_half = prev
        first_half = head

        # Step 3: Interleave/Merge the two halves
        # first_half: 1 -> 2 -> 3
        # second_half: 5 -> 4
        while second_half:
            # Save next nodes
            tmp1 = first_half.next
            tmp2 = second_half.next
            
            # Connect nodes
            first_half.next = second_half
            second_half.next = tmp1
            
            # Move pointers forward
            first_half = tmp1
            second_half = tmp2
            
        return head