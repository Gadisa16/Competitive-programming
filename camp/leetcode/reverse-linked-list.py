# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        point_left= None
        cur= head
        while cur:
            temp_nxt= cur.next
            cur.next = point_left
            point_left= cur
            cur= temp_nxt
        return point_left

        
        