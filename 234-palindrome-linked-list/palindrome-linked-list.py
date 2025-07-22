# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        _cur, leng = head, 0
        while _cur:
            leng +=1
            _cur = _cur.next

        i, prev, cur = 0, None, head
        while cur:
            if i >=leng//2:
                next_node = cur.next
                cur.next = prev
                prev = cur
                cur = next_node
            else:
                cur = cur.next
            i +=1
       
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next

        return True