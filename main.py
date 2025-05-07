# Time Complexity = O(n) we traverse the array once
# Space Complexity = O(n) space for the stack

def validParenthesis(str):
    stack = []

    openToCloseMap = {
        ')': "(",
        "]": '[',
        "}": "{"
    }

    for x in range(len(str)):
        if str[x] in openToCloseMap:
            if stack and openToCloseMap[str[x]] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(str[x])

    return True if not stack else False


if "__main__" == __name__:
    str = "([{])"
    result = validParenthesis(str)
    print(result)
