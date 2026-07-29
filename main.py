def carFleet(target, positions, speeds):
    pairs = [[p, s] for p, s in zip(positions, speeds)]

    stack = []

    pairs.sort()

    for position, speed in pairs[::-1]:
        timeToTarget = (target - position) / speed

        stack.append(timeToTarget)

        if len(stack) > 1 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


if "__main__" == __name__:
    target = 10
    position = [1, 4]
    speed = [3, 2]

    result = carFleet(target, position, speed)
    print(result)
