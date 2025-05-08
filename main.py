# Time Complexity = O(1) we never traverse, constant time for everything
# Space Complexity = O(n) create stacks

def validParenthesis(input):
    openToClose = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    stack = []

    for x in input:
        if x in openToClose:
            if stack and openToClose[x] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(x)

    if stack:
        return False
    else:
        return True


if "__main__" == __name__:
    input = "([{}])"
    result = validParenthesis(input)
    print(result)
