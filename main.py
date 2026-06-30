# Time Complexity: O(n), iterates through list a couple of times but no more than n
# Space Complexity: O(n), creating a result array


def productsOfArrayExceptSelf(nums):
    # first collects prefix, then multiplies them to get final products
    result = []

    prefix = 1

    for i in range(len(nums)):
        if i == 0:
            result.append(prefix)
        else:
            prefix *= nums[i - 1]
            result.append(prefix)

    postfix = 1

    for i in range(len(nums))[::-1]:
        result[i] *= postfix

        postfix *= nums[i]

    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    print(productsOfArrayExceptSelf(nums))
