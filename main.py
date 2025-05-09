# Time Complexity = O(1) we never traverse, constant time for everything
# Space Complexity = O(n) create stacks

class MinStack:

    def __init__(self):
        self.min = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min:
            self.min.append(val)
        else:
            self.min.append(min(self.min[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


if "__main__" == __name__:
    minStack = MinStack()
    minStack.push(1)
    minStack.push(2)
    minStack.push(0)
    minStack.getMin()
    minStack.pop()
    minStack.top()
    minStack.getMin()
