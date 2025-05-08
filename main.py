# Time Complexity = O(1) we never traverse, constant time for everything
# Space Complexity = O(n) create stacks

def threeSum(nums):
    result = []
    nums.sort()

    for x in range(len(nums)):
        if x > 0 and nums[x] == nums[x - 1]:
            continue

        i = x + 1
        j = len(nums) - 1

        while i < j:
            currentSum = nums[x] + nums[i] + nums[j]

            if currentSum < 0:
                i += 1
            elif currentSum > 0:
                j -= 1
            else:
                result.append([nums[x], nums[i], nums[j]])
                i += 1

                while nums[i] == nums[i-1] and i < j:
                    i += 1

    return result


if "__main__" == __name__:
    nums = [1, 2, -2, -1]

    result = threeSum(nums)
    print(result)
