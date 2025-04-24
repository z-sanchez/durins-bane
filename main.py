def threeSum(array):
    result = []
    array.sort()

    for x in range(len(array)):
        if x > 0 and array[x] == array[x - 1]:
            continue

        i = x + 1
        j = len(array) - 1

        while i < j:

            currentSum = array[x] + array[i] + array[j]

            if currentSum > 0:
                j -= 1
            elif currentSum < 0:
                i += 1
            else:
                result.append([array[x], array[i], array[j]])
                i += 1

                if array[i] == array[i - 1] and i < j:
                    i += 1

    return result


if "__main__" == __name__:
    input = [-1, 0, 1, 2, -1, -4]
    print("Input: ", input)
    result = threeSum(input)
    print("Result: ", result)
