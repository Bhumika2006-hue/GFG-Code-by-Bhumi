"""
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""

class Solution:
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head
        
        # Dummy node helps handle the head change easily
        dummy = Node(0)
        dummy.next = head
        prev_group_end = dummy
        
        while True:
            # 1. Find the k-th node (or the end of the list)
            current_group_start = prev_group_end.next
            if not current_group_start:
                break
                
            current_group_end = current_group_start
            # Move current_group_end k-1 steps forward
            for _ in range(k - 1):
                if current_group_end.next:
                    current_group_end = current_group_end.next
                else:
                    break
            
            # Record the start of the next group
            next_group_start = current_group_end.next
            
            # 2. Reverse the segment from current_group_start to current_group_end
            self.reverse_segment(current_group_start, current_group_end)
            
            # 3. Connect the reversed segment back into the list
            prev_group_end.next = current_group_end
            current_group_start.next = next_group_start
            
            # 4. Move prev_group_end for the next iteration
            prev_group_end = current_group_start
            
        return dummy.next

    def reverse_segment(self, start, end):
        """Standard in-place reversal for a sub-segment"""
        prev = None
        curr = start
        stop_node = end.next
        while curr != stop_node:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp