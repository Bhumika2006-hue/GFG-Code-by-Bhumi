class Solution:
    def reverseBetween(self, a, b, head):
        if not head or a == b:
            return head
        
        # Dummy node helps handle the case where a = 1
        dummy = Node(0)
        dummy.next = head
        pre = dummy
        
        # Step 1: Reach the node just before the sublist starts
        for _ in range(a - 1):
            pre = pre.next
            
        # curr will be the first node of the sublist to be reversed
        curr = pre.next
        # next_node will be used for the reversal process
        prev_node = None
        
        # Step 2: Reverse nodes from position a to b
        # We need to perform (b - a + 1) swaps
        tail = curr  # This node will eventually point to the rest of the list
        
        for _ in range(b - a + 1):
            temp = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = temp
            
        # Step 3: Reconnect the reversed sublist
        # pre.next was the original 'a' node, now it should point to 'curr' (the b+1 node)
        pre.next.next = curr
        # pre should now point to the new head of the sublist (prev_node)
        pre.next = prev_node
        
        return dummy.next