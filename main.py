
def threeSum(input):
    sortedInput = sorted(input)
    combinations = []

    for x in range(len(sortedInput)):
        if x > 0 and sortedInput[x] == sortedInput[x - 1]:
            continue

        left = x + 1
        right = len(sortedInput) - 1

        while left < right:
            sum = sortedInput[x] + sortedInput[left] + sortedInput[right]

            if sum == 0:
                combinations.append(
                    [sortedInput[x], sortedInput[left], sortedInput[right]])
                left += 1
                while left < right and sortedInput[left] == sortedInput[left - 1]:
                    left += 1
            elif sum < 0:
                left += 1
            else:
                right -= 1

    return combinations


if "__main__" == __name__:
    input = [-1, 0, 1, 2, -1, -4]

    result = threeSum(input)
    print(result)
