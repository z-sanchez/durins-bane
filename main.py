def trap(input):
    output = 0

    pointer = 0

    while pointer < len(input):
        if input[pointer] == 0:
            pointer += 1
            continue

        # found wall
        pointerToNextWall = pointer + 1
        detectedWater = False
        potentialBlocks = 0

        while pointerToNextWall < len(input):
            if input[pointerToNextWall] == 0:
                detectedWater = True

            if input[pointerToNextWall] < input[pointer]:
                potentialBlocks += input[pointerToNextWall]

            # found trapping wall, greater or equal to current wall
            if input[pointerToNextWall] >= input[pointer] and detectedWater:
                print("trap wall found",
                      input[pointer], "to", input[pointerToNextWall])

                width = pointerToNextWall - pointer - 1
                area = width * min(input[pointerToNextWall], input[pointer])
                print("Counted:", area - potentialBlocks)
                output += area - potentialBlocks
                pointer = pointerToNextWall - 1
                break

            pointerToNextWall += 1

        pointer += 1

    return output


if "__main__" == __name__:
    input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = trap(input)

    print(result)
