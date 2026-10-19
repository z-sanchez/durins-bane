
def carFleet(target, positions, speeds):

    cars = [[pos, speed] for pos, speed in zip(positions, speeds)]

    cars.sort()

    stack = []

    for position, speed in cars[::-1]:
        distanceToTarget = target - position
        timeToTarget = distanceToTarget/speed
        stack.append(timeToTarget)

        if len(stack) > 1 and stack[-2] >= stack[-1]:
            stack.pop()

    return len(stack)


if "__main__" == __name__:
    target = 10
    position = [1, 4]
    speed = [3, 2]

    result = carFleet(target, position, speed)
    print(result)
