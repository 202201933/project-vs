class Stack:
    def __init__(self,size):
        self.size = size
        self.items = []

    def is_full(self):
        if(len(self.items) == self.size):
            return True
        else:
            return False
        
    def is_empty(self):
        if(len(self.items) == 0):
            return True
        else:
            return False
        
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            print("비어있음")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("비어있음")
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)
print(stack[-1])

data = stack.pop()

print(data)
print(stack)

if not stack:
    print("empty")
else:
    print("not empty")