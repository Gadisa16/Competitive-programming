# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy= ListNode(0)
        dummy.next= head
        prev, cur = dummy, head

        def recur(prev, cur):
            if cur:
                if cur.val==val:
                    cur= cur.next
                    prev.next= cur
                    recur(prev, cur)
                else:
                    recur(prev.next, cur.next)

        recur(prev, head)
        return dummy.next  