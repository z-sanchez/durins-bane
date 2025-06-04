

def longestConsecutiveSequence(nums):

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
    nums = [0, 3, 2, 5, 4, 6, 1, 1]

    result = longestConsecutiveSequence(nums)
    print(result)
