class LinkedList:
    def __init__(self, value, next=None, prev=None):
        self.value= value
        self.next= next
        self.prev= prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur= LinkedList(homepage)

    def visit(self, url: str) -> None:
        temp = LinkedList(url)
        temp.prev= self.cur
        self.cur.next= temp
        self.cur= temp
        

    def back(self, steps: int) -> str:
        while steps and self.cur.prev:
            self.cur= self.cur.prev
            steps -=1
        return self.cur.value

    def forward(self, steps: int) -> str:
        while steps and self.cur.next:
            self.cur= self.cur.next
            steps -=1
        return self.cur.value
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)