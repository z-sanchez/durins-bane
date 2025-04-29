def twoSum(nums, target):
    i = 0
    j = len(nums) - 1

    while nums[i] + nums[j] != target:
        currentSum = nums[i] + nums[j]

        if currentSum > target:
            j -= 1
        elif currentSum < target:
            i += 1

    return [i + 1, j + 1]


if "__main__" == __name__:
    input = [0, 2, 3, 4]
    target = 2
    result = twoSum(input, target)
    print(result)
