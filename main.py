# Time Complexity = O(1) we never traverse, constant time for everything
# Space Complexity = O(n) create stacks

def productsOfArrayExceptSelf(nums):

    result = []

    prefix = 1

    for index in range(len(nums)):
        if index == 0:
            result.append(prefix)
        else:
            prefix *= nums[index - 1]
            result.append(prefix)

    print(result)
    postfix = 1

    for i in range(len(nums))[::-1]:
        result[i] *= postfix

        postfix *= nums[i]

    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    print(productsOfArrayExceptSelf(nums))
