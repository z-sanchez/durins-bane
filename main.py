

def longestConsecutive(nums):

    numSet = set(nums)
    result = 0

    for x in numSet:
        if x - 1 not in numSet:
            length = 0
        while x + length in numSet:
            length += 1
        result = max(result, length)

    return result


if "__main__" == __name__:
    nums = [2, 20, 4, 10, 3, 4, 5]

    result = longestConsecutive(nums)
    print(result)
