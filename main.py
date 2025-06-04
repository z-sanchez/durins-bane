

def evalRPN(tokens):

    stack = []

    for x in tokens:
        if x == "+":
            sum = stack.pop() + stack.pop()
            stack.append(sum)
        elif x == "-":
            second = stack.pop()
            first = stack.pop()
            stack.append(first - second)
        elif x == "*":
            stack.append(stack.pop() * stack.pop())
        elif x == "/":
            second = stack.pop()
            first = stack.pop()
            stack.append(int(first / second))
        else:
            stack.append(int(x))

    return stack[0]


if "__main__" == __name__:
    tokens = ["1", "2", "+", "3", "*", "4", "-"]

    result = evalRPN(tokens)
    print(result)
