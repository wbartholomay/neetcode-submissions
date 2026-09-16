# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 0:
            return None
        
        mid = len(lists) // 2
        left_merged = self.mergeKLists(lists[:mid])
        right_merged = self.mergeKLists(lists[mid:])
        return self.conquer(left_merged, right_merged)


    def conquer(self, head_a, head_b):
        head = ListNode(0)
        curr = head
        while head_a and head_b:
            if head_a.val < head_b.val:
                curr.next = head_a
                head_a = head_a.next
            else:
                curr.next = head_b
                head_b = head_b.next
            curr = curr.next
        if head_a:
            curr.next = head_a
        else:
            curr.next = head_b

        return head.next