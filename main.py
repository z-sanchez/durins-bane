def carFleet(target, positions, speeds):
    cars = [[pos, speed] for pos, speed in zip(positions, speeds)]
    stack = []

    for pos, speed in sorted(cars)[::-1]:
        stack.append((target - pos) / speed)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


if "__main__" == __name__:
    target = 10
    position = [1, 4]
    speed = [3, 2]

    result = carFleet(target, position, speed)
    print(result)
