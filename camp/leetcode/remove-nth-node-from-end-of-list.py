# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dNode= ListNode(0)
        dNode.next =head
        l, r= 0, 0
        leftPos= dNode
        cur = dNode
        while cur.next:
            if r>=n:
                l+=1
                r+=1
                leftPos= leftPos.next
            else:
                r +=1
            cur = cur.next
        leftPos.next= leftPos.next.next if leftPos.next else None
        return dNode.next

        

        
        

        