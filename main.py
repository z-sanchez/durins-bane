# Time Complexity: O(n), we traverse the array once max
# Space Complexity: O(1), no new data structure needed


def carFleet(target, position, speed):
    carFleet = []
    stack = [[pos, spee] for pos, spee in zip(position, speed)]

    stack.sort()

    for carPosition, carSpeed in stack[::-1]:
        distanceToTarget = target - carPosition
        timeToTarget = distanceToTarget / carSpeed

        carFleet.append(timeToTarget)

        while len(carFleet) > 1 and carFleet[-2] >= carFleet[-1]:
            carFleet.pop()

    return len(carFleet)


if "__main__" == __name__:
    target = 10
    position = [1, 4]
    speed = [3, 2]

    result = carFleet(target, position, speed)
    print(result)
