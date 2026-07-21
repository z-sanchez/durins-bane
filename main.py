
def threeSum(array):
    result = []

    array.sort()

    for index, num in enumerate(array):
        if index > 0 and array[index - 1] == num:
            continue

        left = index + 1
        right = len(array) - 1

        while left < right:
            sum = num + array[left] + array[right]

            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                result.append([num, array[left], array[right]])

                left += 1

                while left < right and array[left] == array[left - 1]:
                    left += 1

    return result


if "__main__" == __name__:

    array = [-1, 0, 1, 2, -1, -4]

    print(threeSum(array))
