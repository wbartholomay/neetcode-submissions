# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group_head = dummy

        while True:
            kth = self.getKth(prev_group_head, k)
            if not kth:
                break
            next_group_head = kth.next
        
            prev, curr = kth.next, prev_group_head.next
            while curr != next_group_head:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = prev_group_head.next
            prev_group_head.next = kth
            prev_group_head = tmp

        return dummy.next


    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr