# Time Complexity: O(n), we traverse the array once max
# Space Complexity: O(1), no new data structure needed

class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, num):
        if not self.min:
            self.min.append(num)
        else:
            self.min.append(min(self.min[-1], num))

        self.stack.append(num)

    def top(self):
        return self.stack[-1]

    def pop(self):
        self.min.pop()
        self.stack.pop()

    def getMin(self):
        return self.min[-1]


if "__main__" == __name__:
    minStack = MinStack()
    minStack.push(1)
    minStack.push(2)
    minStack.push(0)
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.top())
    print(minStack.getMin())
