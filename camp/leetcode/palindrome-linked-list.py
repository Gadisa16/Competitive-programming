# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        slow, fast= head, head
        while fast and fast.next:
            fast= fast.next.next
            slow= slow.next

        cur, prev= slow, None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        while head and prev:
            if head.val != prev.val:
                return False
            head, prev = head.next, prev.next
        return True
