# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftHead, rightHead = ListNode(0), ListNode(0)
        ltail, rtail =leftHead, rightHead
        while head:
            if head.val< x:
                ltail.next=  head
                ltail =ltail.next
            else:
                rtail.next =head
                rtail =rtail.next
            head =head.next
        rtail.next =None
        ltail.next =rightHead.next
        return leftHead.next
        