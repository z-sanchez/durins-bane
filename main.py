def productOfArray(array):

    before = {}
    after = {}
    result = []

    for x in range(len(array)):
        if x == 0:
            before[x] = 1
            continue

        before[x] = array[x - 1] * before[x - 1]

    for index, value in reversed(list(enumerate(array))):
        if index == len(array) - 1:
            after[index] = 1
            continue

        after[index] = array[index + 1] * after[index + 1]

    for x in range(len(array)):
        result.append(before[x] * after[x])

    return result


if "__main__" == __name__:
    input = [-1, 0, 1, 2, 3]
    productOfArray(input)
