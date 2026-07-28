# Time Complexity: O(n), iterates through list a couple of times but no more than n
# Space Complexity: O(n), creating a result array


def productsOfArrayExceptSelf(nums):
    # first collects prefix, then multiplies them to get final products
    result = []

    prefix = 1

    for num in range(len(nums)):
        if num == 0:
            result.append(prefix)
        else:
            prefix = prefix * nums[num-1]
            result.append(prefix)

    postfix = 1

    for index in range(len(nums))[::-1]:
        result[index] *= postfix

        postfix *= nums[index]

    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    print(productsOfArrayExceptSelf(nums))
