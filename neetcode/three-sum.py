
def threeSum(array):
    result = []

    # prevent duplicates by sorting
    array.sort()

    for i, a in enumerate(array):
        # detect duplicate by comparing prev neighbor
        if i > 0 and a == array[i - 1]:
            continue

        # left is beginning of array, right is end
        l, r = i + 1, len(array) - 1

        # this part is just two sum 2 using a value from array as sum
        while l < r:
            threeSum = a + array[l] + array[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                result.append([a, array[l], array[r]])
                l += 1

                # while left equals its neighbor and won't pass right, advance to prevent duplicate
                # note: must advance left pointer until it equals right to exhaust all possibilities
                while array[l] == array[l - 1] and l < r:
                    l += 1

    return result


if "__main__" == __name__:

    array = [-1, 0, 1, 2, -1, -4]

    threeSum(array)
