# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
            cur, size= head, 0
            while cur:
                size +=1
                cur= cur.next

            decimal= 0
            while head:
                decimal += head.val * 2**(size-1)
                size -=1
                head =head.next
            return decimal