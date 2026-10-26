
def evalRPN(input):

    stack = []

    for entry in input:
        if entry == "+":
            second = stack.pop()
            first = stack.pop()
            stack.append(first + second)
        elif entry == "-":
            second = stack.pop()
            first = stack.pop()
            stack.append(first - second)
        elif entry == "*":
            second = stack.pop()
            first = stack.pop()
            stack.append(first * second)
        elif entry == "/":
            second = stack.pop()
            first = stack.pop()
            stack.append(int(first / second))
        else:
            stack.append(int(entry))

    return stack[0]


if "__main__" == __name__:
    input = ["4", "13", "5", "/", "+"]
    result = evalRPN(input)
    print(result)
