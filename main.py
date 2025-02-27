def twoSum(nums, target):
    i = 0
    j = 1

    while (i < len(nums)):
        while j < len(nums):
            if (nums[i] + nums[j] == target):
                return [i + 1, j + 1]
            j += 1

        i += 1
        j = i + 1


if __name__ == "__main__":
    # these must be least to greatest
    nums = [2, 3, 4]
    target = 6

    # result must be least to greatest
    result = twoSum(nums, target)

    print(result)
