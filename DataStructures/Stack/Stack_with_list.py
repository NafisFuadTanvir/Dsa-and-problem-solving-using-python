stack=[]
def push(stack,item):
    stack.append(item)

def isEmpty(stack):
    return len(stack)==0

def pop(stack):
    return stack.pop()

def peek(stack):
    if isEmpty(stack):
        return "stack is empty"
    else:
        return stack[-1] 



push(stack,"a")
push(stack,"b")
push(stack,"c")
push(stack,"d")
push(stack,"e")

print(stack)

print ("after popping operation:- ")

pop(stack)
print(stack)

print("after peek method apply:- ")

print(peek(stack))
