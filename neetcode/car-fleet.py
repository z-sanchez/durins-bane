# Time Complexity = O(nlogn) we traverse the array once (n) but we do sort the card (longn)
# Space Complexity = O(n) space for the stack

def carFleet(target, positions, speeds):
    # zip combines two array into pairs, use for loop to fill the array using tuples returned
    pair = [[p, s] for p, s in zip(position, speed)]

    # this will keep track of fleet speeds
    stack = []

    # we sort cards to place them on the road in order, [::-1] iterates backwards
    for p, s in sorted(pair)[::-1]:
        # we process a new trailing car
        # we calculate the time it will arrive at target
        # (target - position) = distance to go
        # /s will give you time (/ is for decimal, // is for integer)
        stack.append((target - p) / s)

        # check if enough fleets to compare
        # [-2] is the leading car, [-1] is the trailing
        # if trailing car gets to target before leading, this means it will be forced to go
        # the leading car's speed and become a fleet
        # in this case, we no longer need to keep track of trailing car because the leading one acts
        # as the fleet for both cars
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)


if "__main__" == __name__:
    target = 10
    position = [1, 4]
    speed = [3, 2]

    result = carFleet(target, position, speed)
    print(result)
