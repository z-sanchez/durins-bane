# Time Complexity: O(n), nested loops
# Space Complexity: O(1), creating nothing

def twoSumTwo(array, target):
    # pointer to beginning and pointer to the end
    l, r = 0, len(array) - 1

    # keeps indices from overlapping
    while l < r:
        currentSum = array[l] + array[r]

        if currentSum > target:
            r -= 1
        elif currentSum < target:
            l += 1
        else:
            # wants these results with a 1 based index for some reason
            return [l+1, r+1]

    return []


if "__main__" == __name__:

    # must be in order for it to work
    array = [1, 2, 3, 4]
    target = 3
    result = twoSumTwo(array, target)
    print(result)
