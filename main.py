
def validParenthesis(strInput):
    closeToOpenMap = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    stack = []

    for x in strInput:
        print(stack)
        if x in closeToOpenMap:
            if stack and closeToOpenMap[x] == stack[-1]:
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
    input = "[(])"

    result = validParenthesis(input)
    print(result)
