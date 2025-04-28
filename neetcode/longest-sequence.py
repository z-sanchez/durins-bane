# Time Complexity: O(n), we traverse the array once max
# Space Complexity: O(n), we make a set here

def longestSequence(nums):
    numSet = set(nums)
    result = 0

    for x in nums:
        # means its the start of sequence
        if (x - 1) not in numSet:
            length = 0
            # x + length works because we're dealing in sequences
            while x + length in numSet:
                length += 1
            result = max(result, length)

    return result


if "__main__" == __name__:
    input = [0, 3, 2, 5, 4, 6, 1, 1]
    result = longestSequence(input)
    print(result)
