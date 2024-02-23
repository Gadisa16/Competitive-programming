class MyStack(object):

    def __init__(self):
        self.stack=[]
        

    def push(self, x):
        self.stack.append(x)
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        return self.stack.pop()
        """
        :rtype: int
        """
        

    def top(self):
        return self.stack[-1]
        """
        :rtype: int
        """
        

    def empty(self):
        return len(self.stack)==0
        """
        :rtype: bool
        """
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()