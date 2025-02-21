# Time Complexity: O(n), iterates through list a couple of times but no more than n
# Space Complexity: O(n), creating a result array


def productsOfArrayExceptSelf(nums):
    # first collects prefix, then multiplies them to get final products
    result = []

    # this will collect the product of every value before n (...n)
    prefix = 1

    # iterate through array
    for x in range(len(nums)):
        # if x is first of array, there is no previous value to multiply with prefix
        if x == 0:
            result.append(prefix)
        else:
            # multiply prefix with previous value
            prefix = prefix * nums[x - 1]
            result.append(prefix)

    # prefix array now holds the product of all values prior to any given n

    # we want to do the same thing but for values that come after n
    postfix = 1

    # iterate backwards
    for x in range(len(nums) - 1, -1, -1):
        # use x to find the prefix for this particular index
        # multiply with postfix
        result[x] *= postfix

        # calculate the postfix for next iteration, this will collect the product for all values after any given n
        postfix *= nums[x]

    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    print(productsOfArrayExceptSelf(nums))
