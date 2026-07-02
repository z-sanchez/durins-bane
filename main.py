# Time Complexity: O(m * n)
# Space Complexity: O(m), uses a count map
# m = length of string, n = length of unique characters in string


def productsOfArrayExceptSelf(nums):

    result = []

    prefix = 1

    for i in range(len(nums)):
        if i == 0:
            result.append(prefix)
        else:

            prefix *= nums[i - 1]
            result.append(prefix)

    postfix = 1

    for i in range(len(result))[::-1]:
        result[i] *= postfix
        postfix *= nums[i]

    return result


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, 3]

    print(productsOfArrayExceptSelf(nums))
