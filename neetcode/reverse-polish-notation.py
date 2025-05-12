# Time Complexity: O(n), we traverse the array once max
# Space Complexity: O(n), we create the stack

from typing import List


def evalRPN(tokens: List[str]) -> int:

    stack = []

    for x in tokens:
        if x == '+':
            result = stack.pop() + stack.pop()
            stack.append(result)
        elif x == '-':
            second = stack.pop()
            first = stack.pop()
            stack.append(first - second)
        elif x == '*':
            result = stack.pop() * stack.pop()
            stack.append(result)
        elif x == "/":
            second = stack.pop()
            first = stack.pop()
            # python is floating point division by default, need to make it int
            stack.append(int(first / second))
        else:
            stack.append(int(x))
    # guaranteed a single value by the end based on problem description
    return stack[0]


if "__main__" == __name__:
    input = ["4", "13", "5", "/", "+"]
    result = evalRPN(input)
    print(result)
