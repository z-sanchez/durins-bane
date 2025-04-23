# Time Complexity: O(n), nested loops
# Space Complexity: O(1), creating nothing

def threeSum(array):
    result = []

    array.sort()

    for i in range(len(array)):
        if i > 0 and array[i] == array[i - 1]:
            continue

        l = i + 1
        r = len(array) - 1

        while l < r:
            summed = array[i] + array[l] + array[r]

            if summed > 0:
                r -= 1
            elif summed < 0:
                l += 1
            else:
                result.append([array[i], array[l], array[r]])
                l += 1
                while l < r and array[l] == array[l-1]:
                    l += 1

    return result


if "__main__" == __name__:
    array = [-1, 0, 1, 2, -1, -4]
    output = threeSum(array)
    print("Output: ", output)
