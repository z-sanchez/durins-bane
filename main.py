# Time Complexity = O(nlogn) we traverse the array once (n) but we do sort the card (longn)
# Space Complexity = O(n) space for the stack

def carFleet(target, positions, speeds):
    pairs = [[position, speed] for position, speed in zip(positions, speeds)]
    stack = []
    for position, speed in sorted(pairs)[::-1]:
        distance = (target - position) / speed
        stack.append(distance)

        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


if "__main__" == __name__:
    target = 10
    position = [4, 1, 0, 7]
    speed = [2, 2, 1, 1]

    result = carFleet(target, position, speed)
    print(result)
