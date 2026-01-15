class Solution:
    def getKthFromLast(self, head, k):
        fast = slow = head

        # Move fast pointer k steps ahead
        for _ in range(k):
            if not fast:
                return -1
            fast = fast.next

        # Move both pointers
        while fast:
            slow = slow.next
            fast = fast.next

        return slow.data
