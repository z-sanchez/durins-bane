def longestConsecutiveSequence(nums):
    numSet = set(nums)
    result = 0

    for x in numSet:
        # start of sequence
        if x - 1 not in numSet:
            length = 0
            while x + length in numSet:
                length += 1
            result = max(result, length)

    return result


if __name__ == "__main__":
    # nums = [2, 20, 4, 10, 3, 4, 5]
    # nums = [0, 3, 2, 5, 4, 6, 1, 1]
    nums = [0, -1]

    print(longestConsecutiveSequence(nums))
