# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        setA= set()
        cur = headA
        while cur:
            setA.add(cur)
            cur= cur.next

        curB= headB
        while curB:
            if curB in setA:
                return curB
            curB= curB.next
        

            

        