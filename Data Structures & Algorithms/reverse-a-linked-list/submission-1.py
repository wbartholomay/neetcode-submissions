# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        prev = head
        tmp = head.next
        head.next = None
        while tmp:
            new_tmp = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = new_tmp
        
        return prev
