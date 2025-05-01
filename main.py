def threeSum(input):
    output = []

    input.sort()

    for x in range(len(input)):
        if x > 0 and input[x] == input[x - 1]:
            continue

        i = x + 1
        j = len(input) - 1

        while i < j:
            currentSum = input[x] + input[i] + input[j]

            if currentSum > 0:
                j -= 1
            elif currentSum < 0:
                i += 1
            else:
                output.append([input[x], input[i], input[j]])
                i += 1
                while i < j and input[i] == input[i - 1]:
                    i += 1

    return output


if "__main__" == __name__:
    input = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    result = threeSum(input)

    print(result)
