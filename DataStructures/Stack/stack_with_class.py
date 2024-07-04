class Stack:
    def __init__(self):
        self.items=[]

    def push(self,item):
        self.items.append(item)  

    def isEmpty(self):
        return len(self.items)==0

    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.items.pop()
    
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.items[-1]


_stk= Stack()

_stk.push(10)
_stk.push(20)
_stk.push(30)


print(_stk.peek())
