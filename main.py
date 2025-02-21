# Time Complexity: O(n), iterates through list a couple of times but no more than n
# Space Complexity: O(n), creating a result array


def productsOfArrayExceptSelf(nums):
    result = []

    prefix = 1

    for x in range(len(nums)):
        if x == 0:
            result.append(prefix)
        else:
            prefix *= nums[x - 1]
            result.append(prefix)

    postfix = 1

    for x in range(len(nums) - 1, -1, -1):
        result[x] *= postfix
        postfix *= nums[x]

    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    print(productsOfArrayExceptSelf(nums))
