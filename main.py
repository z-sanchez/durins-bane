
class MinStack:
    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, num):
        if not self.minStack:
            self.minStack.append(num)
        else:
            self.minStack.append(min(self.minStack[-1], num))
        self.stack.append(num)

    def getMin(self):
        return self.minStack[-1]

    def pop(self):
        self.minStack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]


if "__main__" == __name__:
    minStack = MinStack()
    minStack.push(1)
    minStack.push(2)
    minStack.push(0)
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.top())
    print(minStack.getMin())
