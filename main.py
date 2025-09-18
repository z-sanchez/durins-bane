# Time Complexity = O(nlogn) we traverse the array once (n) but we do sort the card (longn)
# Space Complexity = O(n) space for the stack

def carFleet(target, positions, speeds):
    # zip combines two array into pairs, use for loop to fill the array using tuples returned
    pairs = [[pos, speed] for pos, speed in zip(positions, speeds)]
    stack = []

    for position, speed in sorted(pairs)[::-1]:
        time = (target - position) / speed

        stack.append(time)

        while len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


if "__main__" == __name__:
    target = 10
    position = [1, 4]
    speed = [3, 2]

    result = carFleet(target, position, speed)
    print(result)
