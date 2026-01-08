class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
            
        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the linked list
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # Step 3: Compare the first and second halves
        first_half = head
        second_half = prev # 'prev' is the head of the reversed second half
        
        while second_half: # Only need to check the second half
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next
            
        return True