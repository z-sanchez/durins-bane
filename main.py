# Time Complexity = O(1) we never traverse, constant time for everything
# Space Complexity = O(n) create stacks

def longestSequence(nums):

    numSet = set(nums)
    result = 0

    for num in nums:
        if num - 1 not in numSet:
            length = 0
            while length + num in numSet:
                length += 1
            result = max(result, length)

    return result


if "__main__" == __name__:
    input = [0, 3, 2, 5, 4, 6, 1, 1]
    result = longestSequence(input)
    print(result)
