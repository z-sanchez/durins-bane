# Time Complexity: O(n), we traverse the array once max
# Space Complexity: O(1), no new data structure needed

def threeSum(array):
    result = []

    array.sort()

    for index, value in enumerate(array):
        if index > 0 and array[index - 1] == value:
            continue

        left = index + 1
        right = len(array) - 1

        while left < right:
            sum = value + array[left] + array[right]

            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                result.append([value, array[left], array[right]])
                left += 1

                while left < right and array[left] == array[left - 1]:
                    left += 1

    return result


if "__main__" == __name__:

    array = [-1, 0, 1, 2, -1, -4]

    print(threeSum(array))
