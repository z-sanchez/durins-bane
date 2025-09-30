# Time Complexity: O(n^2), nested loops
# Space Complexity: O(n), creating a result array

# The idea here is that you focus on one value at a time. Take that value and find what other two summed with it = 0. Then move to next index.
# We don't have to worry about comparing results using previous array values because those have been exhausted and check for
# Rule of thumb: Once we've passed an index in the array, those values have been checked if there in play already, no need to compare back

def threeSum(array):
    result = []

    array.sort()

    for index, value in enumerate(array):
        if index > 0 and array[index - 1] == value:
            continue

        left = index + 1
        right = len(array) - 1

        while left < right:
            sum = array[left] + array[right] + value

            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                result.append([array[left], array[right], value])

                left += 1

                while left < right and array[left] == array[left - 1]:
                    left += 1
    return result


if "__main__" == __name__:

    array = [-1, 0, 1, 2, -1, -4]

    print(threeSum(array))
