# Time Complexity: O(n), iterates through list a couple of times but no more than n
# Space Complexity: O(n), creating a result array


def productsOfArrayExceptSelf(nums):
    # first collects prefix, then multiplies them to get final products
    result = []

    prefix = 1

    for x in range(len(nums)):
        if x == 0:
            result.append(prefix)
        else:
            prefix *= nums[x-1]
            result.append(prefix)

    postFix = 1

    for x in range(len(result))[::-1]:
        result[x] *= postFix

        postFix *= nums[x]

    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    print(productsOfArrayExceptSelf(nums))
