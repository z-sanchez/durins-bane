# Time Complexity = O(1) we never traverse, constant time for everything
# Space Complexity = O(n) create stacks

class MinStack:

    def __init__(self):
        # stack for actual values
        self.stack = []
        # stack for the corresponding min at that value
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # find minimum to append to the minStack, check if minStack is empty before indexing, else use val
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        # keep both stacks in sync
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # top asks for last element
        return self.stack[-1]

    def getMin(self) -> int:
        # use the corresponding min
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
