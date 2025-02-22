def longestConsecutiveSequence(nums):
    result = 0
    hashSet = set(nums)

    for x in range(len(nums)):
        length = 1
        j = nums[x] + 1
        while j in hashSet:
            length += 1
            j += 1

        result = max(result, length)

    return result


if __name__ == "__main__":
    nums = [2, 20, 4, 10, 3, 4, 5]


print(longestConsecutiveSequence(nums))
