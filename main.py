# Time Complexity: O(n), we traverse the array once max
# Space Complexity: O(1), no new data structure needed

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            self.minStack.append(min(self.minStack[-1], val))

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


if "__main__" == __name__:
    minStack = MinStack()
    minStack.push(1)
    minStack.push(2)
    minStack.push(0)
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.top())
    print(minStack.getMin())
