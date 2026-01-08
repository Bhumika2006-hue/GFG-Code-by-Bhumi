class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def get_length(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def remove_leading_zeros(self, head):
        while head and head.next and head.data == 0:
            head = head.next
        return head

    def subLinkedList(self, l1, l2):
        # 1. Clean leading zeros
        l1 = self.remove_leading_zeros(l1)
        l2 = self.remove_leading_zeros(l2)

        # 2. Find the larger number
        n1, n2 = self.get_length(l1), self.get_length(l2)
        
        if n1 < n2:
            l1, l2 = l2, l1
        elif n1 == n2:
            curr1, curr2 = l1, l2
            while curr1:
                if curr1.data < curr2.data:
                    l1, l2 = l2, l1
                    break
                elif curr1.data > curr2.data:
                    break
                curr1, curr2 = curr1.next, curr2.next

        # 3. Reverse for right-to-left subtraction
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        res_head = None
        borrow = 0
        
        # 4. Perform Subtraction
        c1, c2 = l1, l2
        while c1:
            val1 = c1.data
            val2 = c2.data if c2 else 0
            
            sub = val1 - val2 - borrow
            if sub < 0:
                sub += 10
                borrow = 1
            else:
                borrow = 0
                
            new_node = Node(sub)
            new_node.next = res_head
            res_head = new_node
            
            c1 = c1.next
            if c2: c2 = c2.next

        # 5. Clean result (remove leading zeros created by subtraction)
        res_head = self.remove_leading_zeros(res_head)
        return res_head