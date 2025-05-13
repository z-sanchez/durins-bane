# Time Complexity: O((4^n)/sqrtN), I do not even know
# Space Complexity: O(n), we create the stack

from typing import List


def generateParenthesis(n: int) -> List[str]:
    stack = []
    result = []

    # backtrack to find the possibilities (effectively creates a tree of possibilities)
    def backtrack(openAmount, closedAmount):
        if openAmount == closedAmount == n:
            # turning stack into a string
            result.append("".join(stack))
            return

        # if open amounts are less than n, we can append another open
        if openAmount < n:
            stack.append("(")
            backtrack(openAmount + 1, closedAmount)
            # need to clean up because we use it later
            stack.pop()

        # if closed amounts are less than open, we must close
        if closedAmount < openAmount:
            stack.append(")")
            backtrack(openAmount, closedAmount + 1)
            # need to clean up because we use it later
            stack.pop()

    backtrack(0, 0)
    return result


if "__main__" == __name__:
    input = 3
    result = generateParenthesis(input)
    print(result)
