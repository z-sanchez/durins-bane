# Time Complexity = O(n) we traverse the array once
# Space Complexity = O(n) space for the stack

def validParenthesis(str):

    closeToOpenMap = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    stack = []

    for x in str:
        # check if the char is closing
        if x in closeToOpenMap:
            # if there is a stack and the last element is an open one matching the current close
            if stack and stack[-1] == closeToOpenMap[x]:
                # pop because its valid
                stack.pop()
            else:
                # return false cause it ain't
                return False
        # if not add to stack (LIFO), the most inner parenthesis
        else:
            stack.append(x)

    # return true if stack empty
    return True if not stack else False


if "__main__" == __name__:
    str = "([{}])"
    result = validParenthesis(str)
    print(result)
