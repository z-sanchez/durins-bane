# Time Complexity: O(n), nested loops
# Space Complexity: O(1), creating nothing

def twoSumTwo(array, target):
    l = 0
    r = len(array) - 1

    while array[l] + array[r] != target:
        currentSum = array[l] + array[r]
        if currentSum > target:
            r -= 1
        if currentSum < target:
            l += 1

    return [l + 1, r + 1,]


if "__main__" == __name__:

    # must be in order for it to work
    array = [0, 2, 3, 4]
    target = 3
    result = twoSumTwo(array, target)
    print(result)
