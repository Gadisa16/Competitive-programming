class Node:
    def __init__(self,value=None, next= None, prev= None):
        self.value=value
        self.next= next
        self.prev= prev

class LRUCache:
    def __init__(self, capacity: int):
        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head
        self.capacity=capacity
        self.dic={}

        

    def get(self, key: int) -> int:
        if key in self.dic:
            pre=self.dic[key].prev
            nex=self.dic[key].next
            pre.next=nex
            nex.prev=pre
            self.dic[key].prev=self.tail.prev
            self.dic[key].next=self.tail
            self.tail.prev.next=self.dic[key]
            self.tail.prev=self.dic[key]
            return self.dic[key].value[1]

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.head.next==self.tail:
            temp=Node([key,value])
            self.dic[key]=temp

            self.head.next=temp
            temp.next=self.tail
            self.tail.prev=temp
            temp.prev=self.head
            self.capacity-=1
        else:
            if key in self.dic:
                self.dic[key].value[1]=value
                pre=self.dic[key].prev
                nex=self.dic[key].next
                pre.next=nex
                nex.prev=pre
                self.dic[key].prev=self.tail.prev
                self.dic[key].next=self.tail
                self.tail.prev.next=self.dic[key]
                self.tail.prev=self.dic[key]
            else:
                if self.capacity:
                    temp=Node([key,value])
                    temp.prev=self.tail.prev
                    temp.next=self.tail
                    self.tail.prev.next=temp
                    self.tail.prev=temp
                    self.dic[key] = temp
                    self.capacity-=1
                else:
                    nex=self.head.next.next
                    key_to_delete=self.head.next.value[0]
                    if key_to_delete in self.dic:  
                        del self.dic[key_to_delete]
                    self.head.next=nex
                    nex.prev=self.head

                    temp=Node([key,value])
                    self.dic[key] = temp  
                    temp.prev=self.tail.prev
                    temp.next=self.tail
                    self.tail.prev.next=temp
                    self.tail.prev=temp




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)