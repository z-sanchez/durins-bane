# Time Complexity: O(n), we traverse the array once max
# Space Complexity: O(n), we make a set here

def longestSequence(nums):
    numSet = set(nums)
    result = 0

    for num in numSet:
        if num - 1 not in numSet:
            length = 0
            while num + length in numSet:
                length += 1
            result = max(length, result)

    return result


if "__main__" == __name__:
    input = [0, 3, 2, 5, 4, 6, 1, 1]
    result = longestSequence(input)
    print(result)
