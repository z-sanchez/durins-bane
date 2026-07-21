
def longestSequence(nums):
    result = 0

    for num in nums:
        print(num)
        if num - 1 not in nums:
            length = 0

            while num + length in nums:
                length += 1

            result = max(result, length)

    return result


if "__main__" == __name__:
    input = [2, 20, 4, 10, 3, 4, 5]
    result = longestSequence(input)
    print(result)
