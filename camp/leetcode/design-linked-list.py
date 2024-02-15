class Node:
    def __init__(self, val= None, prev= None, next= None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.left= Node(0)
        self.right= Node(0)
        self.left.next= self.right
        self.right.prev= self.left
        

    def get(self, index: int) -> int:
        cur= self.left.next
        while cur and index > 0:
            cur= cur.next
            index -=1
        if cur and cur != self.right and index==0:
            return cur.val
        return -1
        
    def addAtHead(self, val: int) -> None:
        newN, cur, nxx = Node(val), self.left, self.left.next
        
        cur.next= newN
        newN.prev= cur
        newN.next= nxx
        nxx.prev= newN

    def addAtTail(self, val: int) -> None:
        newN, cur, prvv = Node(val), self.right, self.right.prev

        prvv.next = newN
        newN.prev = prvv
        newN.next= cur
        cur.prev = newN

    def addAtIndex(self, index: int, val: int) -> None:
        cur= self.left.next
        while cur and index >0:
            cur = cur.next
            index -=1
        if cur and index==0:
            newN, prvv= Node(val), cur.prev

            prvv.next= newN
            newN.prev= prvv
            newN.next= cur
            cur.prev= newN

    def deleteAtIndex(self, index: int) -> None:
        cur= self.left.next

        while cur and index >0:
            cur= cur.next
            index -=1
        if cur and cur !=self.right and index==0:
            nxx, prvv= cur.next, cur.prev

            prvv.next= nxx
            nxx.prev= prvv

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)