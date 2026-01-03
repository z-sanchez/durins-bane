# Time Complexity: O(n), nested loops
# Space Complexity: O(1), creating nothing

def carFleet(target, positions, speeds):
    # zip combines two array into pairs, use for loop to fill the array using tuples returned
    pair = [[p, s] for p, s in zip(positions, speeds)]

    # this will keep track of fleet speeds
    stack = []

    for position, speed in sorted(pair)[::-1]:
        time = (target - position) / speed
        stack.append(time)
        if len(stack) > 1 and stack[-2] >= stack[-1]:
            stack.pop()

    return len(stack)


if "__main__" == __name__:
    target = 10
    position = [1, 4]
    speed = [3, 2]

    result = carFleet(target, position, speed)
    print(result)
