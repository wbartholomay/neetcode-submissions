# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group_tail = dummy

        while True:
            curr_group_tail = self.getKth(prev_group_tail, k)
            if not curr_group_tail:
                break
            next_group_head = curr_group_tail.next
            
            prev = curr_group_tail.next
            curr = prev_group_tail.next
            while curr != next_group_head:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = prev_group_tail.next
            prev_group_tail.next = curr_group_tail
            prev_group_tail = tmp
        
        return dummy.next

    
    def getKth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node