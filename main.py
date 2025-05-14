# Time Complexity: O((4^n)/sqrtN), I do not even know
# Space Complexity: O(n), we create the stack

from typing import List


def generateParenthesis(n: int) -> List[str]:
    stack = []
    result = []

    def backtracing(openCount, leftCount):
        if openCount == leftCount == n:
            result.append("".join(stack))
            return

        if openCount > leftCount:
            stack.append(')')
            backtracing(openCount, leftCount + 1)
            stack.pop()

        if openCount < n:
            stack.append('(')
            backtracing(openCount + 1, leftCount)
            stack.pop()

    backtracing(0, 0)

    return result


if "__main__" == __name__:
    input = 3
    result = generateParenthesis(input)
    print(result)
