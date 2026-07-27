# Time Complexity: O(n), we traverse the array once max
# Space Complexity: O(1), no new data structure needed

def productsOfArrayExceptSelf(nums):

    prefix = 1

    result = []

    for index in range(len(nums)):
        if index == 0:
            result.append(prefix)
        else:
            prefix *= nums[index - 1]
            result.append(prefix)

    print(result)

    postfix = 1

    for newIndex in range(len(nums))[::-1]:
        result[newIndex] *= postfix

        postfix *= nums[newIndex]

    return result


if __name__ == "__main__":
    nums = [1, 2, 3, 4]

    print(productsOfArrayExceptSelf(nums))
