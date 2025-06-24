

def threeSum(nums):
    sortedNums = sorted(nums)
    results = []

    for x in range(len((sortedNums))):
        if x > 0 and sortedNums[x] == sortedNums[x - 1]:
            continue

        left = x + 1
        right = len(sortedNums) - 1

        while left < right:
            calculatedSum = sortedNums[x] + \
                sortedNums[left] + sortedNums[right]
            if calculatedSum == 0:
                results.append(
                    [sortedNums[x], sortedNums[left], sortedNums[right]])
                left += 1
                while left < right and sortedNums[left] == sortedNums[left-1]:
                    left += 1
            elif calculatedSum < 0:
                left += 1
            else:
                right -= 1

    return results


if "__main__" == __name__:
    nums = [0, 0, 0]

    result = threeSum(nums)
    print(result)
