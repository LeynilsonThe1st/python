class Stack:
    """
    A stack provides last in/first out (LIFO) data storage.

    stacks == Pilhas
    """

    def __init__(self, size):
        self.max_size = size
        self.data = []

    def push(self, item):
        if len(self.data) < self.max_size:
            self.data.append(item)
            return item
        else:
            return False

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        else:
            return False

    def empty(self):
        return False if len(self.data) > 0 else True

    def full(self):
        return False if len(self.data) < self.max_size else True

    def items(self):
        return self.data


stk = Stack(3)
print("Is empty:", stk.items(), ' == ', stk.empty())
print(stk.push(10), stk.push(20), stk.push(30), stk.push(40))
print("IS full:", stk.items(), ' == ', stk.full())
print(stk.items())
print(stk.pop(), stk.pop(), stk.pop(), stk.pop())
print("IS full:", stk.items(), ' == ', stk.full())
print(stk.push(1), stk.push(2), stk.push(3))
print("IS empty:", stk.items(), ' == ', stk.empty())
