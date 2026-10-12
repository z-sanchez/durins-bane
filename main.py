def getIndices(nums, target):

    left = 0
    right = len(nums) + 1

    result = []

    while left < right:
        sum = nums[left] + nums[right]

        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            return [left+1, right+1]

    return result


if __name__ == "__main__":
    # these must be least to greatest
    nums = [3, 4, 5, 6]
    target = 7

    # result must be least to greatest
    result = getIndices(nums, target)

    print(result)
