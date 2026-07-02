# Time Complexity: O(m * n)
# Space Complexity: O(m), uses a count map
# m = length of string, n = length of unique characters in string


def longestSequence(nums):

    result = 0

    numSet = set(nums)

    for num in nums:
        if num - 1 not in numSet:
            length = 0
            while num + length in numSet:
                length += 1
            result = max(result, length)

    return result


if "__main__" == __name__:
    input = [0, 3, 2, 5, 4, 6, 1, 1]
    result = longestSequence(input)
    print(result)
