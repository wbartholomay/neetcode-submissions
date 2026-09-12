# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
            
        visited = set()
        visited.add(head)
        while head.next:
            next_node = head.next
            if next_node in visited:
                return True
            visited.add(next_node)
            head = next_node
        return False