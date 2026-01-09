class Solution():
    # Function to sort the given doubly linked list using Merge Sort.
    def sort_doubly(self, head):
        # Base case: if list is empty or has only one node
        if not head or not head.next:
            return head
        
        # 1. Split the list into two halves
        mid = self.get_middle(head)
        next_to_mid = mid.next
        mid.next = None
        if next_to_mid:
            next_to_mid.prev = None
        
        # 2. Recursively sort both halves
        left = self.sort_doubly(head)
        right = self.sort_doubly(next_to_mid)
        
        # 3. Merge the sorted halves
        return self.merge(left, right)

    def get_middle(self, head):
        slow = head
        fast = head
        # Fast pointer moves twice as fast as slow pointer
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, first, second):
        # If one of the lists is empty, return the other
        if not first: return second
        if not second: return first
        
        # Pick the smaller value to be the new head
        if first.data <= second.data:
            first.next = self.merge(first.next, second)
            if first.next:
                first.next.prev = first
            first.prev = None
            return first
        else:
            second.next = self.merge(first, second.next)
            if second.next:
                second.next.prev = second
            second.prev = None
            return second