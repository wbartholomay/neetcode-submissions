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
            count = k
            curr_group_tail = prev_group_tail
            while count > 0:
                curr_group_tail = curr_group_tail.next
                if curr_group_tail is None:
                    return dummy.next
                count -= 1
            
            next_group_head = curr_group_tail.next

            prev = next_group_head
            curr = prev_group_tail.next
            while curr != next_group_head:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = prev_group_tail.next
            prev_group_tail.next = curr_group_tail
            prev_group_tail = temp
        
        return dummy.next
