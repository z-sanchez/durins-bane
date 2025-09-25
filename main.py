# Time Complexity: O(n), nested loops
# Space Complexity: O(1), creating nothing

def twoSumTwo(array, target):
    # pointer to beginning and pointer to the end
    l, r = 0, len(array) - 1

    while l < r:
        sum = array[l] + array[r]

        if sum < target:
            l += 1
        elif sum > target:
            r -= 1
        else:
            return [l, r]

    return []


if "__main__" == __name__:

    # must be in order for it to work
    array = [1, 2, 3, 4]
    target = 3
    result = twoSumTwo(array, target)
    print(result)
