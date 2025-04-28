def productOfArray(array):
    left = {}
    right = {}
    result = []

    for x in range(len(array)):
        if x == 0:
            left[x] = 1
            continue

        left[x] = left[x - 1] * array[x - 1]

    for index, value in reversed(list(enumerate(array))):
        if index == len(array) - 1:
            right[index] = 1
            continue

        right[index] = right[index + 1] * array[index + 1]

    for x in range(len(array)):
        result.append(left[x] * right[x])

    return result


if "__main__" == __name__:
    input = [1, 2, 4, 6]
    productOfArray(input)
