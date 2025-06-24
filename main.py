

def carFleet(target, position, speed):
    cars = [[p, s] for p, s in zip(position, speed)]
    stack = []

    for p, s in cars[::-1]:
        stack.append((target - p) / s)

        if len(stack) >= 2 and stack[-1] >= stack[-2]:
            stack.pop()

    return len(stack)


if "__main__" == __name__:
    target = 10
    position = [1, 4]
    speed = [3, 2]

    result = carFleet(target, position, speed)
    print(result)
