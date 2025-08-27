# Time Complexity: O(n), nested loops
# Space Complexity: O(1), creating nothing

def twoSumTwo(array, target):
    left = 0
    right = len(array) - 1

    while left < right:
        sum = array[left] + array[right]

        if sum > target:
            right -= 1
        elif sum < target:
            left += 1
        else:
            return [left + 1, right + 1]

    return []


if "__main__" == __name__:

    # must be in order for it to work
    array = [1, 2, 3, 4]
    target = 3
    result = twoSumTwo(array, target)
    print(result)
