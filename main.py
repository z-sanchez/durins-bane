

def validParenthesis(s):

    stack = []

    closeToOpenMap = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for x in s:
        if x not in closeToOpenMap:
            stack.append(x)
        else:
            if closeToOpenMap[x] == stack[-1]:
                stack.pop()
            else:
                return False

    if stack:
        return False
    else:
        return True


if "__main__" == __name__:
    height = "[(])"

    result = validParenthesis(height)
    print(result)
